import json
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
        self.ast = AssertSetIF(self.project)

    def runner(self, data_type=None, headers=None):
        bp = BasePage(self.file, 1)
        title = bp.get_title()  # 获取用例标题
        datas = bp.params()  # 获取参数
        expected = bp.expected_results()    # 获取预期结果
        self.logger.info('开始%s测试' % title)
        url = self.HOST + bp.url_adress()
        self.logger.info('测试接口：%s' % url)   # 输出接口地址
        h = headers if headers!=None else {'Authorization': 'Token %s' % self.token,
                                           "Content-Type": "application/json"}
        r = bp.send_requests(url, data_type, headers=h, data=datas)  # 发送请求
        return_code = str(r.status_code)    # 获取返回码
        self.ast.assertEqual(return_code, str(expected['code']).replace(' ', ''),
                             '-----返回码：%s' % return_code)   # 判断返回码是否正确
        return_data = r.json().get('data')  # 获取返回数据
        self.ast.assertIn(str(expected['data']), str(return_data),
                          '-----返回数据：%s' % return_data)
        self.logger.info('--------------------------------------------------------------')

    def false_log(self):
        false_list = set(self.false_list)
        print(false_list)


if __name__ == '__main__':
    project = 'SupplierManagement'
    file = 'Data_of_sample.xlsx'
    test = SupplierManagementTest(project, file)
    test.runner('json')









