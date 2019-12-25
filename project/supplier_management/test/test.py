import unittest

from config.main_pathes import PROJECTINFO
from project.supplier_management.common.project_path import DATA_PATH
from utils.basePage import BasePage
from utils.fileReader import YamlReader, ExcelReader
from utils.getToken import get_token


class SupplierManagementTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.num = 0
        self.file = '%s\IFcase_SupplierManagement.xlsx' % DATA_PATH
        self.project = 'SupplierManagement'  # 定义项目
        self.token = get_token(self.project)  # 获取TOKEN
        self.HOST = YamlReader(PROJECTINFO).get(self.project).get('HOST')  # 获取HOST

    def test_runner(self):
        max_row = ExcelReader(self.file).max_rows
        print(max_row)
        self.bp = BasePage(self.file, self.num)
        url = self.HOST + self.bp.url_adress()
        datas = self.bp.params()
        headers = {'Authorization': 'Token %s' % self.token}
        r = self.bp.send_requests(url, headers=headers, json=datas)
        print(r.text)

    @classmethod
    def tearDownClass(self):
        pass


if __name__ == '__main__':
    unittest.main()