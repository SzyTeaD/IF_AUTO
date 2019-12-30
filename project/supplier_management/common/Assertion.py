from utils.log import Logger


class AssertSetIF(object):
    def __init__(self, project):
        self.project = project
        self.logger = Logger(self.project).get_logger()

    def assertIn(self, member, container):
        try:
            if member in container:
                self.logger.info('测试通过')
            else:
                raise AssertionError
        except Exception:
            standardMsg = '%s not found in %s' % (member, container)
            self.logger.error('测试未通过:%s' % standardMsg)

    def assertEqual(self, par1, par2):
        try:
            if par1 == par2:
                self.logger.info('测试通过')
            else:
                raise AssertionError
        except Exception:
            standardMsg = '%s is not %s' % (par1, par2)
            self.logger.error('测试未通过:%s' % standardMsg)

    def assertNotIn(self, member, container):
        try:
            if member not in container:
                self.logger.info('测试通过')
            else:
                raise AssertionError
        except Exception:
            standardMsg = '%s found in %s' % (member, container)
            self.logger.error('测试未通过:%s' % standardMsg)

    def assertNotEqual(self, par1, par2):
        try:
            if par1 != par2:
                self.logger.info('测试通过')
            else:
                raise AssertionError
        except Exception:
            standardMsg = '%s == %s' % (par1, par2)
            self.logger.error('测试未通过:%s' % standardMsg)


if __name__ == '__main__':
    a = AssertSetIF('SupplierManagement')
    a.assertIn('saf', 'gssdga')



