# -*- coding: UTF-8 -*-

from MYunit.myunit import Myunit
from yewushitu.loginPage import LoginPage


class LoginTestCast(Myunit):
    #UI_test_0804/data/user.csv
    filePath = '../data/user.csv'
    def testLogin1(self):
        l = LoginPage(self.n_dirver)
        l.loginAction('17600570787','3edc@WSX')
        self.assertTrue(l.checkLoginStatus())



    def testLogin2(self):
        l = LoginPage(self.n_dirver)

        # 读取csv里面的参数
        row = l.get_csv_data(csv_file=self.filePath, line=1)
        #logger.info(row[0])

        # 调用登录的函数进行登录操作
        l.loginAction(row[0], row[1])

        # 添加断言,,,
        self.assertTrue(l.checkLoginStatus())