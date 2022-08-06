import csv
import random
import time

from selenium.webdriver.common.keys import Keys

from MYunit.myunit import logger


class PageObject(object):
    # 初始化，获取驱动
    def __init__(self, s_driver):
        self.driver = s_driver

    def find_element(self, *args):
        return self.driver.find_element(*args)

    # 查找多个元素
    def find_elements(self, *args):

        return self.driver.find_elements(*args)

    # 获取时间
    def getTime(self):
        self.now = time.strftime('%Y-%m-%d %H_%M_%S')
        return self.now

    # 获取截图的操作..desc..描述截图来自哪里/信息
    # login_20190122094526.png
    def getScreenShot(self, desc):
        image_file = 'UI_test_0804/screenshots' + str(
            desc) + '_' + self.getTime() + '.png'
        logger.info(str(desc) + '生成截图')
        print((str(desc) + '生成截图'))
        self.driver.get_screenshot_as_file(image_file)

    # 该函数是获取excel表格某一行数据用的
    # csv_file要读取的那个csv文件, line读取的哪一行数据...该行数从1开始...5
    def get_csv_data(self, csv_file, line):
        logger.info('---------------获取csv数据-----------------')
        print('---------------获取csv数据-----------------')
        file = open(csv_file, 'r', encoding='utf-8-sig')

        # 把csv读取的所有数据放到了reader对象里面
        reader = csv.reader(file)

        # 需要的是某一行的数据...enumerate(reader,1)作用就是把reader(列表)里面的数据列举出来,并且制定角标从1开始
        for index, row in enumerate(reader, 1):
            if index == line:
                return row

    def time_Sleep(self, *args):
        return time.sleep(*args)

    # 从多个元素中找到唯一需要的元素，并点击
    def find_elements_one_click(self, name, *args):

        elementslist1 = self.driver.find_elements(*args)
        for elment in elementslist1:
            if elment.is_displayed() == True:
               # logger.info(elment.text)
                if elment.text == name:
                    return elment.click()

    # 从多个无用元素中，找到唯一需要的元素，并点击
    def find_element_one_click(self, *args):
        elementlist = self.find_elements(*args)
        try:
            for i in elementlist:
                if i.is_displayed() == True:
                    return i.click()
        except BaseException:
            print('报错')
        else:
            pass

    # 从多个空元素中，根据下标找到可用元素
    def find_elements_list(self, *args, num):
        list = self.driver.find_elements(*args)
        return list[num].click()

    # 从多个空元素中，根据下标找到可用元素并输入内容
    def find_elements_input(self, *args, index, num):
        list = self.driver.find_elements(*args)
        return list[index].send_keys(num)

    def random_itemList(self, *args):
        list = self.driver.find_elements(*args)
        l = len(list)
        i = random.randint(0, l)
        return list[i].click(),logger.info(list[i].text)

    def inputName(self, name, *args):
        dc2Input = self.find_element(*args)
        print(len(dc2Input.get_attribute('value')))

        if (len(dc2Input.get_attribute()) > 0):
            dc2Input.send_keys(Keys.BACKSPACE)
        return dc2Input.send_keys(name)

    def refresh(self):
        return self.refresh()

    def current_url(self, urlinput):
        url = self.driver.current_url
        if url == urlinput:
            return True
        else:
            return False

    def element_input(self, Element, *args):
        list = self.find_elements(*args)
        for l in list:
            if l.is_displayed() == True:
                if l.text == Element:
                    return l.click()
                #logger.info(l.text),

    def set_scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

