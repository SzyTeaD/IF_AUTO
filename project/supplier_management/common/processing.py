from config.main_pathes import PROJECTINFO
from project.supplier_management.common.assertion import AssertSetIF
from project.supplier_management.common.project_path import DATA_PATH
from utils.basePage import BasePage, GetCase
from utils.fileReader import YamlReader, ExcelReader
from utils.getToken import get_token
from utils.log import Logger


class Processing(object):
    def __init__(self, project, filename, rows=None):
        """
        :param project: 在配置文件中配置项目名称
        :param filename: 用例文件名称
        :param rows: 执行用例数，默认为全部执行
        """
        self.project = project  # 定义项目
        self.file = "%s\\" % DATA_PATH + filename
        self.ast = AssertSetIF(self.project)
        self.token = get_token(self.project)  # 获取TOKEN
        self.failList = self.ast.failList
        self.logger = Logger(self.project).get_logger()
        self.HOST = YamlReader(PROJECTINFO).get(self.project).get('HOST')  # 获取HOST
        self.maxCaseNum = rows if rows else int(ExcelReader(self.file).max_rows)-3

    def runner(self, headers=None):
        for i in range(test.maxCaseNum):
            case = GetCase(self.file, self.project, i)
            bp = BasePage(case)
            title = case.get_title()  # 获取用例标题
            boby = case.params()  # 获取参数
            expected = case.expected_results()    # 获取预期结果
            self.logger.info('%s.开始%s测试' % (int(i)+1, title))
            url = self.HOST + case.api()
            self.logger.info('测试接口: %s' % url)   # 输出接口地址
            h = headers if headers!=None else {"Authorization": "Token %s" % self.token,
                                               "Content-Type": "application/json",
                                               "Connection": "keep-alive"}
            r = bp.send_requests(url, h, boby)  # 发送请求
            return_code = str(r.status_code)    # 获取返回码
            self.ast.assertEqual(str(expected['code']).replace(' ', ''), return_code,
                                 '用例编号%s; 返回码：%s' % (int(i)+1, return_code))   # 判断返回码是否正确
            return_data = r.json().get('data')  # 获取返回数据
            self.ast.assertIn(str(expected['data']), str(return_data),
                              '用例编号%s; 返回参数：%s' % (int(i)+1, r.json()))   # 判断返回值是否正确
            self.logger.info('------------------------本条用例执行结束------------------------')

    def case_situation(self):
        faliNum = 0
        from project.supplier_management.common.project_fail_log import FailLogger
        failLog = FailLogger(self.project).get_logger()
        failLog.info('本次未通过的用例：')
        for i in self.failList:
            failLog.error(i)
            faliNum += 1
        fail_rate = '%s%%' % ((self.maxCaseNum-faliNum)/self.maxCaseNum*100)
        self.logger.info('执行用例总数：%s条，失败用例数：%s条,用例通过率：%s' % (self.maxCaseNum, faliNum, fail_rate))


if __name__ == '__main__':
    project = 'SupplierManagement'
    file = 'data_of_sample.xlsx'
    test = Processing(project, file,1)
    test.runner()
    test.case_situation()











