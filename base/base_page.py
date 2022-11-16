import logging
from time import sleep
from base.logToHandle import test_log
from selenium import webdriver
from selenium.webdriver.common.by import By
log = test_log()
path = '/Users/junbo.zjb/Downloads/chromedriver'

class BasePage:
    #driver = webdriver.Chrome()
    #实例化BasePage类时，事先执行init方法，该方法需要传递参数
    def __init__(self, driver):
        log.info('初始化driver{}'.format(driver))
        self.driver = driver

    #访问网页
    def visit(self):
        log.info('正在打开网页{}'.format(self.url))
        self.driver.get(self.url)

    #元素定位
    def locator(self, loc):
        log.info('正在元素定位{}'.format(loc))
        return self.driver.find_element(*loc)
    #输入
    def input_(self, loc, txt):
        log.info('正在输入{}'.format(loc, txt))
        self.locator(loc).send_keys(txt)
    #点击
    def click(self,loc):
        log.info('正在点击按钮{}'.format(loc))
        self.locator(loc).click()
    #等待
    def wait(self, time_):
        sleep(time_)
    #清除
    def clear_text(self,loc):
        self.locator(loc).clear()
    #表单切换
    def switch_iframe(self,loc):
        self.driver.switch_to.frame(self.locator(loc))
    #窗口切换
    def switch_window(self,n):
        self.driver.switch_to.window(self.driver.window_handles[n])
