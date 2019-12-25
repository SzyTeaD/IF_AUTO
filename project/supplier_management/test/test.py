import ast
import json

import requests

from config.main_pathes import PROJECTINFO
from project.supplier_management.common.project_path import DATA_PATH
from utils.basePage import BasePage
from utils.fileReader import YamlReader
from utils.getToken import get_token


class SupplierManagementTest():
    def __init__(self):
        file = '%s\IFcase_SupplierManagement.xlsx' % DATA_PATH
        self.bp = BasePage(file)
        self.project = 'SupplierManagement'  # 定义项目
        self.token = get_token(self.project)  # 获取TOKEN
        self.HOST = YamlReader(PROJECTINFO).get(self.project).get('HOST')  # 获取HOST


    def test1_params_list(self):
        url = self.HOST + self.bp.url_adress()
        datas = self.bp.params()
        headers = {'Authorization': 'Token %s' % self.token}
        r = self.bp.send_requests(url, headers=headers, json=datas)
        print(r.text)


if __name__ == '__main__':
    test = SupplierManagementTest()
    test.test1_params_list()