# coding:utf-8

import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print "S"

    @classmethod
    def tearDownClass(cls):
        print "E"

    def setUp(self):
        print "test case start"

    def tearDown(self):
        print "test case end"

    @unittest.skip("直接跳过")
    def test_case1(self):
        print "test case 1"

    @unittest.skipIf(3 > 2, "条件为True时执行")
    def test_case2(self):
        print "test case 2"


if __name__ == "__main__":
    unittest.main()
