import unittest
from time import sleep

from selenium import webdriver
import warnings

from page_obect.index_page import IndexPage
from page_obect.login_page import LoginPage
from ddt import ddt,  file_data, data


#测试用例设计
@ddt
class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @file_data('../data/user.yaml')
    def test_1_login(self,username, password):
        self.lp.login(username, password)
        sleep(5)

    @data('手机', '钱包')
    def test_2_search(self, txt):
        self.ip.search(txt)
        sleep(3)

    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)


if __name__ == '__main__':
    unittest.main()