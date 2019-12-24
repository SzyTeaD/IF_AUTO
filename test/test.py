import json

import requests

from config.pathes import PROJECTINFO, DATA_PATH
from utils.FileReader import YamlReader, ExcelReader
from utils.getToken import get_token

head = {'Authorization': 'Token %s' % get_token('ETPSS')}
ex = ExcelReader(DATA_PATH+'\供应商接口测试.xls').data[0]
url = YamlReader(PROJECTINFO).get('ETPSS').get('HOST') + ex.get('url')
print(ex.get('参数'))
pars = ex.get('参数')

par = {
    "type": "0"
}

r = requests.get(url, headers=head,params=par)
print(r.text)