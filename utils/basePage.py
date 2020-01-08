import ast
import json

import requests

from config.main_pathes import PROJECTINFO
from utils.assertion import AssertSetIF
from utils.fileReader import ExcelReader, YamlReader
from utils.log import Logger


class BasePage(object):
    def __init__(self, project):
        """
        :param project: 在配置文件中配置项目名称
        """
        self.res = requests
        self.project = project  # 初始化项目
        self.ast = AssertSetIF(self.project)    # 初始化断言
        self.logger = Logger(self.project).get_logger()  # 初始化日志
        self.HOST = YamlReader(PROJECTINFO).get(self.project).get('HOST')  # 初始化Host

    def send_requests_by_excel(self, file, rows=None, headers=None):
        """
        :param filename: 用例文件名称
        :param rows: 执行用例数，默认为全部执行
        :param headers: 请求头
        """
        self.maxCaseNum = rows if rows else int(ExcelReader(file).max_rows)-3
        for i in range(self.maxCaseNum):
            case = GetCase(file, self.project, i)
            title = case.get_title()  # 获取用例标题
            boby = case.params()  # 获取参数
            expected = case.expected_results()    # 获取预期结果
            request_method = case.get_request_method()  # 获取请求方式
            data_type = case.get_data_type()    # 获取数据类型
            self.logger.info('%s.开始%s测试' % (int(i)+1, title))
            url = self.HOST + case.api()
            self.logger.info('测试接口: %s' % url)   # 输出接口地址
            h = {"Authorization": "Token %s" % self.get_token(),
                 "Content-Type": "application/json",
                 "Connection": "keep-alive"} if headers==None else headers
            r = self.send_requests(url, h, request_method, boby, data_type)  # 发送请求
            return_code = str(r.status_code)    # 获取返回码
            self.ast.assertEqual(str(expected['code']).replace(' ', ''), return_code,
                                 '用例编号%s; 返回码：%s' % (int(i)+1, return_code))   # 判断返回码是否正确
            return_data = r.json().get('data')  # 获取返回数据
            self.ast.assertIn(str(expected['data']), str(return_data),
                              '用例编号%s; 返回参数：%s' % (int(i)+1, r.json()))   # 判断返回值是否正确
            self.logger.info('------------------------本条用例执行结束------------------------')
        self.case_by_excel_situation()

    def send_requests(self, url, headers, request_method, boby=None, data_type=None, **kwargs):
        if request_method == 'get':
            r = self.res.get(url, headers=headers, params=boby, **kwargs)
            return r
        elif request_method == 'post':
            if data_type == 'json':
                r = self.res.post(url, headers=headers, json=boby, **kwargs)  # 发送请求
                return r
            elif data_type == 'data':
                r = self.res.post(url, headers=headers, data=json.dumps(boby), **kwargs)  # 发送请求
                return r
            else:
                print("不支持%s类型数据格式，仅支持json和text" % data_type)
        else:
            raise TypeError('不支持%s类型请求，请尝试post或者get方式' % request_method)

    def get_token(self):
        p = YamlReader(PROJECTINFO).get(self.project)['token'] if self.project else YamlReader(PROJECTINFO)
        url = p.get('url') if p and p.get('url') else YamlReader(PROJECTINFO).get('token')['url']
        headers = p.get('head') if p and p.get('head') else YamlReader(PROJECTINFO).get('token')['head']
        boby = p.get('data') if p and p.get('data') else YamlReader(PROJECTINFO).get('token')['data']
        r = requests.post(url, data=json.dumps(boby), headers=headers)
        t = r.json()
        return t['data']['access_token']

    def case_by_excel_situation(self):
        from project.supplier_management.common.project_fail_log import FailLogger
        faillist = self.ast.failList
        faliNum = 0
        failLog = FailLogger(self.project).get_logger()
        failLog.info('本次未通过的用例：')
        for i in faillist:
            failLog.error(i)
            faliNum += 1
        fail_rate = '%s%%' % ((self.maxCaseNum - faliNum) / self.maxCaseNum * 100)
        self.logger.info('执行用例总数：%s条，失败用例数：%s条,用例通过率：%s' % (self.maxCaseNum, faliNum, fail_rate))


class GetCase(object):
    def __init__(self, file, project, i=0):
        """
        :param file: 用例文件路径
        :param project: 项目名称
        :param i: 执行用例编号
        """
        self.file = file
        self.num = i
        self.project = project
        self.excel = ExcelReader(self.file)

    def workBook(self):
        # 获取用例
        workbook = self.excel.data[self.num]
        return workbook

    def get_title(self):
        # 获取标题，默认第一行
        title = self.workBook().get('用例标题')
        return title

    def api(self):
        # 获取url地址，默认第一行
        api = self.workBook().get('前置条件')
        return api

    def params(self):
        # 获取参数，默认第一行
        params = self.workBook().get('步骤')
        if params == 'None':
            pass
        else:
            return ast.literal_eval(params)

    def expected_results(self):
        # 读取预期结果，默认第一行
        expected_results = self.workBook().get('预期')
        return ast.literal_eval(expected_results)

    def get_request_method(self):
        # 获取方法
        method = ast.literal_eval(self.workBook().get('关键词'))
        return method['request_method']

    def get_data_type(self):
        method = ast.literal_eval(self.workBook().get('关键词'))
        return method['data_type']

    def max_rows(self):
        max_rows = self.excel.max_rows
        return max_rows


class ExpectedReturn(object):
    pass


if __name__ == '__main__':
    project = 'SupplierManagement'
    bp = BasePage(project)
    h = {"Authorization": "Token %s" % bp.get_token(), "Content-Type": "application/json"}
    url = 'http://106.74.152.35:13249/1/srm/config_list'
    boby = {"1": [{"520": "供应商类型1"}, {"521": "供应商类型2"}], "2": [{"522": "供货类型1"}, {"523": "供货类型2"}],
            "3": [{"524": "供应商级别1"}, {"525": "供应商级别2"}]}
    filename = 'F:\PyCharm\py_work\IF_AOTO\project\supplier_management\data\data_of_sample.xlsx'
    # bp.send_requests_by_excel(filename)
    r = bp.send_requests(url, h, 'get', boby)
    print(r.json())
