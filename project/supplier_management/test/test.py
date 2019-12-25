import unittest

from config.main_pathes import PROJECTINFO
from project.supplier_management.common.mail import Mail
from project.supplier_management.common.project_path import DATA_PATH
from utils.basePage import BasePage
from utils.fileReader import YamlReader, ExcelReader
from utils.getToken import get_token
from utils.log import Logger


class SupplierManagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.num = None
        self.file = '%s\IFcase_SupplierManagement.xlsx' % DATA_PATH
        self.project = 'SupplierManagement'  # 定义项目
        self.token = get_token(self.project)  # 获取TOKEN
        self.HOST = YamlReader(PROJECTINFO).get(self.project).get('HOST')  # 获取HOST
        self.logger = Logger(self.project).get_logger()

    def test_runner(self):
        max_row = ExcelReader(self.file).max_rows
        for i in range(max_row):
            self.bp = BasePage(self.file, i)
            url = self.HOST + self.bp.url_adress()
            datas = self.bp.params()
            headers = {'Authorization': 'Token %s' % self.token}
            r = self.bp.send_requests(url, headers=headers, json=datas)
            logger(r.text)

    @classmethod
    def tearDownClass(self):
        eml = Mail(self.project)
        eml.send_mail()


if __name__ == '__main__':
    unittest.main()