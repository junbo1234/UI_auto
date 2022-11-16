from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver
path = '/Users/junbo.zjb/Downloads/chromedriver'
from base.base_page import BasePage


class LoginPage(BasePage):
    url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    user = (By.NAME, 'accounts')
    password = (By.NAME, 'pwd')
    login_button = (By.XPATH, '/html[1]/body[1]/div[4]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]')

    def login(self, username, pwd):
        self.visit()
        self.input_(self.user, username)
        self.input_(self.password, pwd)
        self.click(self.login_button)

#调试
# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     username = 'xuzhu666'
#     password = '123456'
#     lp = LoginPage(driver)
#     lp.login(username, password)

# sleep(5)
# driver.quit()