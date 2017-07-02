# coding:utf-8

import unittest


class MyClass(unittest.TestCase):
    def setUp(self):
        print "Testcase start!"

    def tearDown(self):
        print "Testcase end!"
