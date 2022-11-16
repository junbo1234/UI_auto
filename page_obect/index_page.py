'''
实现首页中搜索
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class IndexPage(BasePage):
    url = 'http://39.98.138.157/shopxo/index.php'

    search_input = (By.NAME, 'wd')
    search_botton = (By.XPATH, '/html[1]/body[1]/div[3]/div[1]/div[3]/form[1]/div[1]/input[2]')

    def search(self, txt):
        self.visit()
        self.input_(self.search_input, txt)
        self.click(self.search_botton)

'''
if __name__ == '__main__':
    driver = webdriver.Chrome()
    txt = '手机'
    ip = IndexPage(driver)
    ip.search(txt)
'''