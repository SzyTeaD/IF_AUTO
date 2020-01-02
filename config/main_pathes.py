"""
文件路径
"""
import os
import time

DAY = time.strftime('%Y-%m-%d',time.localtime(time.time()))
TIME = time.strftime(' %H-%M-%S',time.localtime(time.time()))
NOW = DAY + TIME
HOME_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH = os.path.join(HOME_PATH, 'config')
LOG_PATH = os.path.join(HOME_PATH, 'log')
USERINFO = os.path.join(CONFIG_PATH, 'UserInfo.yml')
PROJECTINFO = os.path.join(CONFIG_PATH, 'ProjectInfo.yml')


if __name__ == '__main__':
    print(HOME_PATH)
    print(CONFIG_PATH)
    print(USERINFO)
    print(PROJECTINFO)

