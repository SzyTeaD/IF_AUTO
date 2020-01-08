import unittest

from utils.basePage import BasePage


class SupplierIFTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        project = 'SupplierManagement'
        self.test = BasePage(project)
        print('测试开始：')

    def test1_run_by_excel(self):
        try:
            file = 'F:\PyCharm\py_work\IF_AOTO\project\supplier_management\data\data_of_sample.xlsx'
            self.test.send_requests_by_excel(file)
        except Exception:
            print('测试阻塞')

    def test2_run(self):
        url = 'http://106.74.152.35:13249/1/srm/config_list'
        h = {"Authorization": "Token %s" % self.test.get_token(), "Content-Type": "application/json"}
        r = self.test.send_requests(url, h, 'get')
        print(r.json())

    @classmethod
    def tearDownClass(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()