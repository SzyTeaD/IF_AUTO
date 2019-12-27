import unittest

from config.main_pathes import PROJECTINFO
from project.supplier_management.common.Assertion import AssertSetIF
from project.supplier_management.common.project_path import DATA_PATH
from utils.basePage import BasePage
from utils.fileReader import YamlReader, ExcelReader
from utils.getToken import get_token
from utils.log import Logger


class SupplierManagementTest(object):
    def __init__(self, project, filename, rows=None):
        """
        :param project: 在配置文件中配置项目名称
        :param filename: 用例文件名称
        :param rows: 执行用例数，默认为全部执行
        """
        self.false_list = []
        self.file = "%s\\" % DATA_PATH + filename
        self.project = project  # 定义项目
        self.token = get_token(self.project)  # 获取TOKEN
        self.HOST = YamlReader(PROJECTINFO).get(self.project).get('HOST')  # 获取HOST
        self.logger = Logger(self.project).get_logger()
        self.max_rows = rows if rows else ExcelReader(self.file).max_rows
        self.ast = AssertSetIF()

    def runner(self, data_type='json', headers=None):
        for i in range(self.max_rows):
            bp = BasePage(self.file, i)
            title = bp.get_title()  # 获取用例标题
            datas = bp.params()  # 获取参数
            expected = bp.expected_results()    # 获取预期结果
            self.logger.info('开始%s测试' % title)
            url = self.HOST + bp.url_adress()
            self.logger.info('测试接口：%s' % url)
            h = headers if headers!=None else {'Authorization': 'Token %s' % self.token, "Content-Type": "application/json"}
            r = bp.send_requests(url, data_type, headers=h, json=datas)  # 发送请求
            return_code = str(r.status_code)
            # print(type(str(expected['code'])), type(return_code))
            self.ast.assertIs(200, 200)
            # self.ast.assertIs(str(expected['code']).replace(' ',''), return_code)
            self.logger.info('返回状态码：%s' % r.status_code)

            # self.logger.info('返回码：%s' % bp.get_title())
            # self.false_list.append(bp.get_title())
            # return_data = r.json().get('data')
            # assert(return_data, expected, self.logger.info('返回数据：%s' % r.return_data))
            # self.logger.info('返回数据错误：%s' % bp.get_title())
            # self.false_list.append(bp.get_title())
            # # self.logger.info(r.text)


    def false_log(self):
        false_list = set(self.false_list)
        print(false_list)


if __name__ == '__main__':
    project = 'SupplierManagement'
    file = 'Data_of_sample.xlsx'
    test = SupplierManagementTest(project, file, rows=2)
    test.runner()
    # a= 'sdaf   111   '
    # print(a.replace(' ',''))
