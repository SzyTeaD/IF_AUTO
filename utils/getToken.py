import requests
import json

from config.pathes import PROJECTINFO
from utils.FileReader import YamlReader


def get_token(project=None):
    p = YamlReader(PROJECTINFO).get(project)['token'] if project else YamlReader(PROJECTINFO)
    url = p.get('url') if p and p.get('url') else YamlReader(PROJECTINFO).get('token')['url']
    head = p.get('head') if p and p.get('head') else YamlReader(PROJECTINFO).get('token')['head']
    data = p.get('data') if p and p.get('data') else YamlReader(PROJECTINFO).get('token')['data']
    r = requests.post(url, data=json.dumps(data), headers=head)
    t = r.json()
    return t['data']['access_token']


if __name__ == '__main__':
    token = get_token()
    print(token)
