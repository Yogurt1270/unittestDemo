# coding:utf-8

from calculator import Count
from myclass import MyClass


class TestSub(MyClass):
    def test_sub(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_sub(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)
