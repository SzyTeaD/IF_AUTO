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
        title = self.bp.get_title()
        url = self.HOST + self.bp.url_adress()
        expected_results = self.bp.expected_results()
        par = self.bp.params()
        head = {'Authorization': 'Token %s' % self.token}
        data = {
            "type": "0"
        }
        r = requests.get(url, headers=head, params=data)
        print(r.text)


if __name__ == '__main__':
    test = SupplierManagementTest()
    test.test1_params_list()