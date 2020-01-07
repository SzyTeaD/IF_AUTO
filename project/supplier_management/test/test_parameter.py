import unittest

from project.supplier_management.common.processing import Processing


class SupplierIFTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('测试开始：')

    def test1_parmeter(self):
        project = 'SupplierManagement'
        file = 'data_of_sample.xlsx'
        dr = Processing(project, file)
        try:
            for i in range(dr.maxCaseNum):
                dr.runner(i)
        except Exception:
            print('测试阻塞')
        dr.case_situation()

    @classmethod
    def tearDownClass(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()