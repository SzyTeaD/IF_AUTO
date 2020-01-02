from utils.log import Logger


class AssertSetIF(object):
    def __init__(self, project):
        self.project = project
        self.failList = []
        self.logger = Logger(self.project).get_logger()

    def assertIn(self, member, container, msg=''):
        try:
            if member in container:
                self.logger.info('测试通过: %s' % msg)
            else:
                raise AssertionError
        except Exception:
            expectedMsg = '预期结果: %s' % (member)
            failMsg = ('测试未通过: %s, %s' % (msg, expectedMsg))
            self.logger.error(failMsg)
            self.failList.append(failMsg)


    def assertEqual(self, par1, par2, msg=''):
        try:
            if par1 == par2:
                self.logger.info('测试通过: %s' % msg)
            else:
                raise AssertionError
        except Exception:
            expectedMsg = '预期结果: %s' % (par1)
            failMsg = ('测试未通过: %s, %s' % (msg, expectedMsg))
            self.logger.error(failMsg)
            self.failList.append(failMsg)

    def assertNotIn(self, member, container, msg=''):
        try:
            if member not in container:
                self.logger.info('测试通过: %s' % msg)
            else:
                raise AssertionError
        except Exception:
            expectedMsg = '预期结果: %s' % (member)
            failMsg = ('测试未通过: %s, %s' % (msg, expectedMsg))
            self.logger.error(failMsg)
            self.failList.append(failMsg)

    def assertNotEqual(self, par1, par2, msg=''):
        try:
            if par1 != par2:
                self.logger.info('测试通过: %s' % msg)
            else:
                raise AssertionError
        except Exception:
            expectedMsg = '预期结果: %s' % (par1)
            failMsg = ('测试未通过: %s, %s' % (msg, expectedMsg))
            self.logger.error(failMsg)
            self.failList.append(failMsg)


if __name__ == '__main__':
    a = AssertSetIF('SupplierManagement')
    a.assertIn('saf', 'gssdga')
    print(a.failList)



