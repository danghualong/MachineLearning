#encoding=utf-8

from factorial import Factorial
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.__fact=Factorial()
    def test_1(self):
        actual=self.__fact.multiply(1)
        self.assertEquals(1,actual)
    def test3(self):
        actual=self.__fact.multiply(3)
        self.assertEquals(6,actual)

class IllegalTestCase(unittest.TestCase):
    def setUp(self):
        self.__fact=Factorial()

    def test_Minus1(self):
        actual=self.__fact.multiply(-1)
        self.assertEquals(1,actual)

    def test_9(self):
        self.assertRaises(Exception,self.__fact.multiply,9)
