"""
文件路径
"""
import os


PROJECT_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
HOME_PATH = os.path.split(os.path.split(PROJECT_PATH)[0])[0]
DATA_PATH = os.path.join(PROJECT_PATH, 'data')
REPORT_PATH = os.path.join(PROJECT_PATH, 'report')
CASE_PATH = os.path.join(os.path.join(PROJECT_PATH,'test'), 'case')
FAIL_LOG_PATH = os.path.join(PROJECT_PATH, 'faillog')


if __name__ == '__main__':
    print(PROJECT_PATH)
    print(DATA_PATH)
    print(REPORT_PATH)
    print(CASE_PATH)

