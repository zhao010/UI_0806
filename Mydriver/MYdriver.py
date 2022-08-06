#coding = utf-8

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def my_driver():
    # 创建chrome参数对象
    #opt = webdriver.ChromeOptions()
    opt = Options()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    #opt.set_headless()
    opt.add_argument('--headless')
    opt.add_argument('--no-sandbox')
    opt.add_argument('--disable-dev-shm-usage')
    opt.add_argument('--disable-gpu')
    opt.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    #opt.add_argument("--remote-debugging-port=9222")
    mdriver = webdriver.Chrome(executable_path = '/usr/bin/chromedriver',chrome_options=opt)
    mdriver.maximize_window()
    mdriver.implicitly_wait(10)
    return mdriver
