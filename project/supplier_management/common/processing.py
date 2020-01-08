from project.supplier_management.common.project_fail_log import FailLogger
from utils.assertion import AssertSetIF


def case_situation(project):
    ast = AssertSetIF(project)
    faillist = ast.failList
    faliNum = 0
    failLog = FailLogger(project).get_logger()
    failLog.info('本次未通过的用例：')
    for i in faillist:
        failLog.error(i)
        faliNum += 1
    fail_rate = '%s%%' % ((maxCaseNum-faliNum)/maxCaseNum*100)
    logger.info('执行用例总数：%s条，失败用例数：%s条,用例通过率：%s' % (self.maxCaseNum, faliNum, fail_rate))


if __name__ == '__main__':
    project = 'SupplierManagement'
    file = 'F:\PyCharm\py_work\IF_AOTO\project\supplier_management\data\data_of_sample.xlsx'











