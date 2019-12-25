from project.supplier_management.common.project_path import DATA_PATH
from utils.fileReader import ExcelReader


class BasePage(object):
    def __init__(self, file, num=0):
        self.num = num
        self.file = file
        self.excel = ExcelReader(self.file)

    def workbook(self):
        # 获取用例
        workbook = self.excel.data[self.num]
        return workbook

    def get_title(self):
        # 获取标题，默认第一行
        title = self.workbook().get('用例标题')
        return title

    def url_adress(self):
        # 获取url地址，默认第一行
        url_adress = self.workbook().get('前置条件')
        return url_adress

    def params(self):
        # 获取参数，默认第一行
        params = self.workbook().get('步骤')
        return params

    def expected_results(self):
        # 读取预期结果，默认第一行
        expected_results = self.workbook().get('预期')
        return expected_results

    def get_method(self):
        # 获取预期结果，默认第一行
        method = self.workbook().get('关键词')
        return method

    def max_rows(self):
        max_rows = self.excel.max_rows
        return max_rows


if __name__ == '__main__':
    file = '%s\IFcase_SupplierManagement.xlsx' % DATA_PATH
    bp = BasePage(file)
    print(bp.get_method())