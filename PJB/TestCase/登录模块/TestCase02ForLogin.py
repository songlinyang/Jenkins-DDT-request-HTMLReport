import unittest
import traceback
import requests
from ddt import ddt,file_data
from time import sleep

@ddt
class TestCase01ForLogin(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #测试用例1：用户名和密码正确
    def test_login01(self):
        pass

    #测试用例2：用户名或密码错误
    def test_login02(self):
        pass

    #测试用例3：用户名为空
    def test_login03(self):
        pass

    #测试用例4：密码为空
    def test_login04(self):
        pass

    #测试用例5：用户名和密码为空
    def test_login05(self):
        pass




if __name__ == '__main__':
