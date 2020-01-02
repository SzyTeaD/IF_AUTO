
import os
import logging
from logging.handlers import TimedRotatingFileHandler

from config.main_pathes import DAY
from project.supplier_management.common.project_path import FAIL_LOG_PATH


class FailLogger(object):
    def __init__(self, progect):
        self.progect = progect
        self.logger_name = '%s_Fail' % self.progect
        self.logger = logging.getLogger(self.logger_name)
        logging.root.setLevel(logging.NOTSET)
        if not os.path.exists(FAIL_LOG_PATH):
            os.mkdir(FAIL_LOG_PATH)
        self.log_file_name = '%s %s_fail_log.log' % (DAY, self.progect)     # 日志文件
        self.backup_count = 10  # 保留的日志数量
        self.console_output_level = 'ERROR'   # 日志输出级别
        self.file_output_level = 'ERROR'
        pattern = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'    # 日志输出格式
        self.ft = logging.Formatter(pattern)

    def remove_log(self):
        """删除多余日志"""
        while True:
            lists = os.listdir(FAIL_LOG_PATH)
            log_count = len(set(lists))
            if log_count <= self.backup_count:
                break
            else:
                lists.sort(key=lambda fn: os.path.getmtime(FAIL_LOG_PATH))
                old_log_file = os.path.join(FAIL_LOG_PATH, lists[0])
                os.remove(old_log_file)

    def get_logger(self):
        if not self.logger.handlers:  # 避免重复日志
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.ft)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)
            self.remove_log()   # 每天重新创建一个日志文件，最多保留backup_count份
            lf = TimedRotatingFileHandler(filename=os.path.join(FAIL_LOG_PATH, self.log_file_name),
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            lf.setFormatter(self.ft)
            lf.setLevel(self.file_output_level)
            self.logger.addHandler(lf)
        return self.logger


if __name__ == '__main__':
    FailLogger('SupplierManagement').get_logger().error('doooo')