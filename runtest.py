# coding:utf-8

from testadd import TestAdd
from testsub import TestSub
import unittest

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


if __name__ == "__name__":
    '''
        # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestAdd("test_add"))
    suite.addTest(TestAdd("test_add2"))
    suite.addTest(TestSub("test_sub"))
    suite.addTest(TestSub("test_sub2"))
    '''

    # 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(discover)
