import os
import sys
import time
import unittest

root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)

from case.login_testcase import LoginTestCast

from unittest import runner
from unittest import suite

from run_case import HTMLTestRunner

print(sys.path)
if __name__ == '__main__':
    # 测试套件
    suite = unittest.TestSuite()
    # 添加测试用例
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(LoginTestCast))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    # reports/20190123145923.html
    path = '../repoet/'+str(time.strftime('%Y-%m-%d %H_%M_%S'))+'.html'
    file = open(path,'wb')
    # 获取一个运行器
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title='自动化测试报告',description='滴滴云自动化测试')
    # 运行
    runner.run(suite)
