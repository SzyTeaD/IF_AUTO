from config.main_pathes import PROJECTINFO
from utils.assertion import AssertSetIF
from project.supplier_management.common.project_path import DATA_PATH
from utils.basePage import BasePage, GetCase
from utils.fileReader import YamlReader, ExcelReader
from utils.getToken import get_token
from utils.log import Logger


class Processing(object):
    def __init__(self, project, filename=None, rows=None):
        pass

    def case_situation(self):
        pass
        # faliNum = 0
        # from project.supplier_management.common.project_fail_log import FailLogger
        # failLog = FailLogger(self.project).get_logger()
        # failLog.info('本次未通过的用例：')
        # for i in self.failList:
        #     failLog.error(i)
        #     faliNum += 1
        # fail_rate = '%s%%' % ((self.maxCaseNum-faliNum)/self.maxCaseNum*100)
        # self.logger.info('执行用例总数：%s条，失败用例数：%s条,用例通过率：%s' % (self.maxCaseNum, faliNum, fail_rate))


if __name__ == '__main__':
    project = 'SupplierManagement'
    file = 'data_of_sample.xlsx'
    test = Processing(project, file)
    test.runner_by_excel()
    test.case_situation()











