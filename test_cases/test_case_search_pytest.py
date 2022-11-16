import pytest
from time import sleep

from selenium import webdriver
import warnings

from page_obect.index_page import IndexPage
from page_obect.login_page import LoginPage
from config.yamlload import loadyml
'''
class中前置后置函数的运行顺序：
setup class
setup method
setup
teardown
teardown method
teardown class
'''

'''
    pytest中用例的管理手段：mark
    可以通过mark装饰器对所有用例进行标记，不同标记区分管理
@pytest.mark.webui   
def test_01():
    print('web01')
    
@pytest.mark.webui      
def test_02():
    print('web02')

@pytest.mark.inui      
def test_03():
    print('inter03')
    
if __name__ == '__main__':
    pytest.main()

运行：pytest -m webui，就会只执行01、02的webui标记的用例
    
'''



#测试用例设计
class TestCase():

    def setup_class(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.lp = LoginPage(cls.driver)
        cls.ip = IndexPage(cls.driver)

    #loginPage测试用例
    @pytest.mark.parametrize('udata', loadyml('../data/user.yaml'))
    def test_1_login(self,udata):
        self.lp.login(udata['username'], udata['password'])
        sleep(5)

    @pytest.mark.parametrize('usearch', loadyml('../data/search.yaml'))
    def test_2_search(self, usearch):
        self.ip.search(usearch['search'])
        sleep(3)

    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)

    def teardown_class(cls) -> None:
        sleep(2)
        cls.driver.quit()


if __name__ == '__main__':
    pytest.main()

#生成测试报告
