# coding=utf-8
'''
Created on 2016-7-26
@author: Jennifer
Project:整合自动发邮件功能，执行测试用例生成最新测试报告，取最新的测试报告，发送最新测试报告
问题，邮件始终不能显示html：将电脑时间改为北京时间即可
'''
import unittest
import os
import sys
import time
import os
import smtplib
root_path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_path)
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from case.login_testcase import LoginTestCast
from run_case import HTMLTestRunner


def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '/' + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    #    L=file_path.split('\\')
    #    file_path='\\\\'.join(L)
    return file_path


# 3.定义：发送邮件，发送最新测试报告html
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 调试使用
    #    print u'打印'
    #    print mail_body
    # 关闭文件
    f.close()

    #邮箱15330276178@163.com  密码zhiyuan0932
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户名/密码 ----设置自己邮箱变成服务邮箱--需要设置
    user = '17600570787@163.com'
    password = 'AUQQGOUSXGOJCLYQ'
    # 发送邮箱
    sender = '17600570787@163.com'
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receiver = ['zhaozhansheng_v@didiglobal.com']
    # 发送邮件主题
    subject = '自动定时发送测试报告'+time.strftime('%Y%m%d%H%M%S')

    # 编写 HTML类型的邮件正文
    # MIMEText这个效果和下方用MIMEMultipart效果是一致的，已通过。
    #    msg = MIMEText(mail_body,'html','utf-8')

    msg = MIMEMultipart('mixed')

    # 注意：由于msg_html在msg_plain后面，所以msg_html以附件的形式出现
    #    text = "Dear all!\nThe attachment is new testreport.\nPlease check it."
    # 中文测试ok
    #    text = "Dear all!\n附件是最新的测试报告。\n麻烦下载下来看，用火狐浏览器打开查看。\n请知悉，谢谢。"
    #    msg_plain = MIMEText(text,'plain', 'utf-8')
    #    msg.attach(msg_plain)

    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)

    # 以附件的方式发送：但是会报554，倍163退信。--此路不通。
    #    msg_html = MIMEText(mail_body,'base64','utf-8')
    #    msg_html["Content-Type"] = 'application/octet-stream'
    #    msg_html.add_header('Content-Disposition', 'attachment', filename='testreport.html')
    #    msg.attach(msg_html)

    # 要加上msg['From']这句话，否则会报554的错误。
    # 要在163有限设置授权码（即客户端的密码），否则会报535
    msg['From'] = '17600570787@163.com <17600570787@163.com>'
    #    msg['To'] = 'XXX@doov.com.cn'
    # 多个收件人
    msg['To'] = ";".join(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    # 连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver, 25)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    print
    '=====AutoTest Start======'
    test_report_dir = '../repoet'
    suite = unittest.TestSuite()
    #CSDN--别倒错------------------------------------------------------
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LoginTestCast))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CreatTestCase))
    #suite.addTests(unittest.TestLoader().loadTestsFromTestCase(CreatEBSTestCase))
    #  定义生成测试报告的名称
    filename1 = r"" + str(time.strftime('%Y%m%d%H%M%S')) + ".html"
    fp = open(test_report_dir+"/"+filename1, 'wb')
    # 定义测试报告的路径，标题，描述等内容
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'自动化测试报告')
    runner.run(suite)
    # 注意：调用函数一定要加括号，一个括号害死个人，哎，查了几天的问题，才发现导致html文件始终显示空白，就是因为close函数调用不正确，漏了括号。
    fp.close()
    # 2.取最新测试报告
    new_report = new_file(test_report_dir)
    #    print new_report

    # 3.发送邮件，发送最新测试报告html
    send_email(new_report)
    print
    '=====AutoTest Over======'
