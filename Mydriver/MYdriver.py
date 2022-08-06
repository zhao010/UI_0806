#coding = utf-8

from selenium import webdriver


def my_driver():
    # 创建chrome参数对象
    opt = webdriver.ChromeOptions()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    opt.set_headless()
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    mdriver = webdriver.Chrome('/usr/bin/chromedriver',options=opt)
    mdriver.maximize_window()
    mdriver.implicitly_wait(10)
    return mdriver
