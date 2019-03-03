"""这是一个测试用例集"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from PJB.TestReport import HTMLTestRunner
from unittest import TestSuite
import requests
from ddt import ddt,data, unpack
import json
import traceback



@ddt
class TestCase01ForLogin(unittest.TestCase):

    def body_to_dict(self,body):
        body_dict = {}
        if body is not None:
            body_str = str(body, encoding="utf-8")
            # 字符串转成字典
            body_dict = json.loads(body_str)
            return body_dict
        else:
            return body_dict

    def get_request_by_key(self,req,key):
        if key is not None:
            value = None
            try:
                value = req[key]
            except KeyError:
                value = None
            return value
        else:
            traceback.print_exc()
            return None

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def user_login_action(self,username,password,imagecode):
        url_path = "https://www.pj.com/pj-common/login"
        payload = {"username":username,"password":password,"imageCode":imagecode,"clientType":"WEB"}
        req = requests.post(url=url_path,json=payload)
        body1 = req.content
        print("body---》",body1)
        response = self.body_to_dict(body1)
        return response

    #DDT数据驱动
    @data(["admin","","123","验证码计算错误"],
          ["13715384224","haha123","111111","登录成功"])
    #测试用例1：测试验证码校验功能
    @unpack
    def test_login01(self,username,password,imagecode,result):
        #测试步骤
        request = self.user_login_action(username,password,imagecode)
        #实际结果
        actual_result = self.get_request_by_key(request, "retMsg")
        #预期结果
        expect_result = result
        self.assertEqual(actual_result,expect_result)


    def test_login02(self):
        pass


    def test_login03(self):
        pass


    def test_login04(self):
        pass


    def test_login05(self):
        pass




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestCase01ForLogin("test_login01"))
    suite.addTest(TestCase01ForLogin("test_login02"))
    suite.addTest(TestCase01ForLogin("test_login03"))
    suite.addTest(TestCase01ForLogin("test_login04"))
    suite.addTest(TestCase01ForLogin("test_login05"))
    report = open("./report.html",'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=report, verbosity=1, title="接口自动化测试", description="登录模块的测试")
    runner.run(suite)