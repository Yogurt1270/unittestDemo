# coding:utf-8

from testadd import TestAdd
from testsub import TestSub
import unittest

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')


if __name__ == "__name__":

    # 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(discover)
