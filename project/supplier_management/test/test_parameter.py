import unittest

from project.supplier_management.common.processing import Processing


class SupplierIFTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('测试开始：')

    def test1_parmeter(self):
        project = 'SupplierManagement'
        file = 'Data_of_sample.xlsx'
        dr = Processing(project, file)
        try:
            for i in range(dr.maxCaseNum):
                dr.runner(i)
        except Exception:
            print('失败')
        dr.fail_log()

    @classmethod
    def tearDownClass(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()