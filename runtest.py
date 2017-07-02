# coding:utf-8

import unittest

test_dir = "./unittestDemo/testcase"
discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__ == "__main__":

    # 执行测试用例
    runner = unittest.TextTestRunner()
    runner.run(discover)
