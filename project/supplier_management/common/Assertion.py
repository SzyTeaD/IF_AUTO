import time
import unittest


class AssertSetIF(object):
    def __init__(self):
        self.failureException = AssertionError

    def formatMessage(self, msg, standardMsg):
        try:
            return '%s : %s' % (standardMsg, msg)
        except UnicodeDecodeError:
            return '%s : %s' % (standardMsg, msg)

    def fail(self, msg=None):
        raise self.failureException(msg)

    def assertIn(self, member, container, msg=None):
        if member not in container:
            standardMsg = '%s not found in %s' % (member, container)
            self.fail(self.formatMessage(msg, standardMsg))

    def assertIs(self, par1, par2, msg=None):
        if par1 != par2:
            standardMsg = '%s is not %s' % (par1, par2)
            self.fail(self.formatMessage(msg, standardMsg))

class f1(unittest.TestCase):
    def a(self):
        self.assertIs()