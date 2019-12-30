from utils.log import Logger


class AssertSetIF(object):
    def __init__(self, project):
        self.project = project
        self.logger = Logger(self.project).get_logger()
        self.failureException = AssertionError


    def fail(self,msg):
        raise self.failureException(msg)

    def assertIn(self, member, container):
        if member not in container:
            standardMsg = '%s not found in %s' % (member, container)
            self.fail(standardMsg)

    def assertIs(self, par1, par2):
        try:
            par1 == par2
            self.logger.info('测试通过')
        except:
            standardMsg = '%s is not %s' % (par1, par2)
            self.logger.error(self.fail(standardMsg))



if __name__ == '__main__':
    a = AssertSetIF('SupplierManagement')
    a.assertIs('200', 200)
    # try:
    #     a.assertIn('DG1sd', 'aGDSGSADGsdgasdg0ASF0')
    # except:
    #     print(24)

# class f1(unittest.TestCase):
#     def a(self):
#         self.assertIs()
#
