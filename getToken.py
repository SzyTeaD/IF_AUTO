import requests
import json

from config.pathes import PROJECTINFO
from utils.FileReader import YamlReader


def get_token(url,head,data):
    p = YamlReader(PROJECTINFO).get('ETPSS')
    url = p.get('tokenUrl') if p and p.get('tokenUrl') else '1'
    head = {"Content-Type": "application/json"}
    data = {
            "user_id": 10000041150702,
            "client_id": "4g0ucoqrwtn92dxq",
            "grant_type": "application_code",
            "scope": "app_scope"
    }
    r = requests.post(url, data=json.dumps(data), headers=head)
    t = r.json()
    return t['data']['access_token']


if __name__ == '__main__':
    token = get_token()
    print(token)