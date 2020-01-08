import unittest

from project.supplier_management.common.processing import Processing
from utils.getToken import get_token


class SupplierIFTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('测试开始：')

    def test1_run_by_excel(self):
        try:
            project = 'SupplierManagement'
            file = 'data_of_sample.xlsx'
            test = Processing(project, file)
            test.runner_by_excel()
            test.case_situation()
        except Exception:
            print('测试阻塞')

    def test2_run(self):
        project = 'SupplierManagement'
        url = 'http://106.74.152.35:13249/1/srm/config_list'
        h = {"Authorization": "Token %s" % get_token(project), "Content-Type": "application/json"}
        test = Processing(project)
        r = test.runner(url, 'get', h)
        print(r.json())

    @classmethod
    def tearDownClass(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()