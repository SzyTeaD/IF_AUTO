import requests

from project.supplier_management.common.project_path import PROJECTINFO, DATA_PATH
from utils.FileReader import YamlReader, ExcelReader
from utils.getToken import get_token






head = {'Authorization': 'Token %s' % get_token('ETPSS')}
print(DATA_PATH+'\IFcase_SupplierManagement.xlsx')
ex = ExcelReader(DATA_PATH+'\IFcase_SupplierManagement.xlsx').data[0]
url = YamlReader(PROJECTINFO).get('ETPSS').get('HOST') + ex.get('前置条件')
print(ex.get('步骤'))
pars = ex.get('步骤')

par = {
    "type": "0"
}
'F:\PyCharm\py_work\IF_AOTO\data\IFcase_SupplierManagement.xlsx'
r = requests.get(url, headers=head, params=par)
print(r.text)