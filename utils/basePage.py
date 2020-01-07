import ast
import json

import requests

from project.supplier_management.common.project_path import DATA_PATH
from utils.fileReader import ExcelReader
from utils.getToken import get_token


class BasePage(object):
    def __init__(self, case=None):
        """
        :param case:用例。case不为空时，需添加用例文件到指定目录下（data）
        """
        self.res = requests
        self.case = case

    def send_requests(self, url, headers=None, request_type=None, data_type=None, data=None, **kwargs):
        request_type = self.case.get_resType() if self.case else request_type
        data_type = self.case.get_dataType() if self.case else data_type
        data = self.case.params() if self.case else data
        if request_type == 'get':
            r = self.res.get(url, headers=headers, params=data, **kwargs)
            return r
        elif request_type == 'post':
            if data_type == 'json':
                r = self.res.post(url, headers=headers, json=data, **kwargs)  # 发送请求
                return r
            elif data_type == 'data':
                r = self.res.post(url, headers=headers, data=json.dumps(data), **kwargs)  # 发送请求
                return r
            else:
                print("不支持%s类型数据格式，仅支持json和text" % data_type)
        else:
            raise TypeError('不支持%s类型请求，请尝试post或者get方式' % request_type)


class GetCase(object):
    def __init__(self, file, project, i=0):
        """
        :param file: 用例文件名称
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
            print('未传参数')
        else:
            return ast.literal_eval(params)

    def expected_results(self):
        # 读取预期结果，默认第一行
        expected_results = self.workBook().get('预期')
        return ast.literal_eval(expected_results)

    def get_resType(self):
        # 获取方法
        method = ast.literal_eval(self.workBook().get('关键词'))
        return method['request_type']

    def get_dataType(self):
        method = ast.literal_eval(self.workBook().get('关键词'))
        return method['data_type']

    def max_rows(self):
        max_rows = self.excel.max_rows
        return max_rows


class ExpectedReturn(object):
    pass


if __name__ == '__main__':
    file = '%s\data_of_sample.xlsx' % DATA_PATH
    project = 'SupplierManagement'
    case = GetCase(file, project, 1)
    bp = BasePage(case)
    h = {"Authorization": "Token %s" % get_token(project), "Content-Type": "application/json"}
    url = 'http://106.74.152.35:13249/1/srm/config_save'
    r = bp.send_requests(url, h)
    print(r.json())
    bp2 = BasePage()
    boby = {"1": [{"520": "供应商类型1"},{"521": "供应商类型2"}],"2": [{"522": "供货类型1"},{"523": "供货类型2"}],
            "3": [{"524": "供应商级别1"},{"525": "供应商级别2"}]}
    r2 = bp2.send_requests(url, h, 'post', 'json', boby)
    print(r2.json())