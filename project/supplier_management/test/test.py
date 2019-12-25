import unittest

from config.main_pathes import PROJECTINFO
from project.supplier_management.common.project_path import DATA_PATH
from utils.basePage import BasePage
from utils.fileReader import YamlReader, ExcelReader
from utils.getToken import get_token
from utils.log import Logger


class SupplierManagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.num = None
        self.false_list = []
        self.file = '%s\IFcase_SupplierManagement.xlsx' % DATA_PATH
        self.project = 'SupplierManagement'  # 定义项目
        self.token = get_token(self.project)  # 获取TOKEN
        self.HOST = YamlReader(PROJECTINFO).get(self.project).get('HOST')  # 获取HOST
        self.logger = Logger(self.project).get_logger()

    def test_runner(self):
        max_row = ExcelReader(self.file).max_rows
        for i in range(max_row):
            bp = BasePage(self.file, i)
            # self.logger.info('开始%s测试' % bp.get_title())
            url = self.HOST + bp.url_adress()
            # self.logger.info('测试接口：%s' % url)
            datas = bp.params()  # 获取参数
            headers = {'Authorization': 'Token %s' % self.token,
                       "Content-Type": "application/json"
                       }
            r = bp.send_requests(url, headers=headers, json=datas)  # 发送请求
            expected = bp.expected_results()    # 获取预期结果
            return_code = str(r.status_code)
            try:
                self.assertIn(return_code, expected, self.logger.info('返回状态码：%s' % r.status_code))
            except Exception:
                self.logger.info('返回码：%s' % bp.get_title())
                self.false_list.append(bp.get_title())
            return_data = r.json().get('data')
            try:
                self.assertIn(return_data, expected, self.logger.info('返回数据：%s' % r.return_data))
            except Exception:
                self.logger.info('返回数据错误：%s' % bp.get_title())
                self.false_list.append(bp.get_title())
            # self.logger.info(r.text)

    @classmethod
    def tearDownClass(self):
        false_list = set(self.false_list)
        print(false_list)


if __name__ == '__main__':
    unittest.main()