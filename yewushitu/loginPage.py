from selenium.webdriver.common.by import By

from PAgeobject.pageobject import PageObject


class LoginPage(PageObject):
    # 当前这个页面所需要的元素查找都写到最上面
    usernameInput = (By.CSS_SELECTOR, 'input[placeholder="151xxxxx789/example@didiyun.com"]')
    passwordInput = (By.CSS_SELECTOR, 'input[type="password"]')
    button = (By.CSS_SELECTOR, 'button[type="submit"]')
    router_link = (By.CSS_SELECTOR, 'div[class="cur-tag router-link-exact-active router-link-active"]')

    def loginAction(self, username, password):
        self.driver.get("https://app.didiyun.com/#/")
        #logger.info('-----------开始打开首页-------------')
        self.find_element(*self.usernameInput).send_keys(username)
        self.find_element(*self.passwordInput).send_keys(password)
        print('---------------点击登录按钮,开始登录------------------')
        self.find_element(*self.button).click()
        self.time_Sleep(6)

    def checkLoginStatus(self):
        text = self.find_element(*self.router_link).text
        if text == '概览':
            print('----------登录成功------------')
            return True
        else:
            self.getScreenShot('loginFail')
            #logger.info('----------登录失败,截图------------')
            return False