import ast
import json

import requests

from project.supplier_management.common.project_path import DATA_PATH
from utils.fileReader import ExcelReader
from utils.log import Logger


class BasePage(object):
    def __init__(self, file, project, num=0):
        """
        :param file: 用例文件名称
        :param project: 项目名称
        :param num: 执行用例数量
        """
        self.num = num
        self.file = file
        self.excel = ExcelReader(self.file)
        self.res = requests
        self.project = project  # 定义项目
        self.logger = Logger(self.project).get_logger()


    def workBook(self):
        # 获取用例
        workbook = self.excel.data[self.num]
        return workbook

    def get_title(self):
        # 获取标题，默认第一行
        title = self.workBook().get('用例标题')
        return title

    def url_adress(self):
        # 获取url地址，默认第一行
        url_adress = self.workBook().get('前置条件')
        return url_adress

    def params(self):
        # 获取参数，默认第一行
        params = self.workBook().get('步骤')
        if params == 'None':
            self.logger.warn('未传入参数')
        else:
            return ast.literal_eval(params)

    def expected_results(self):
        # 读取预期结果，默认第一行
        expected_results = self.workBook().get('预期')
        return ast.literal_eval(expected_results)

    def get_resType(self):
        # 获取方法
        method = ast.literal_eval(self.workBook().get('关键词'))
        return method['request_type']

    def get_dataType(self):
        method = ast.literal_eval(self.workBook().get('关键词'))
        return method['data_type']

    def max_rows(self):
        max_rows = self.excel.max_rows
        return max_rows

    def send_requests(self, url, headers=None, data=None, **kwargs):
        if self.get_resType() == 'get':
            r = self.res.get(url, headers=headers, params=data, **kwargs)
            return r
        elif self.get_resType() == 'post':
            if self.get_dataType() == 'json':
                r = self.res.post(url, headers=headers, json=json.dumps(data), **kwargs)  # 发送请求
                return r
            elif self.get_dataType() == 'data':
                r = self.res.post(url, headers=headers, data=data, **kwargs)  # 发送请求
                return r
            else:
                print("请确认您的数据格式，仅支持json和text")
        else:
            raise TypeError('不支持此类型请求，请尝试post或者get方式')


if __name__ == '__main__':
    file = '%s\IFcase_SupplierManagement.xlsx' % DATA_PATH
    bp = BasePage(file)
    # print(bp.get_method())
    bp.send_requests('put')