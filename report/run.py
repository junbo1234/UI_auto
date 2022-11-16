#生成测试报告
#下载commandline包(https://github.com/allure-framework/allure2/releases)，放到python安装路径
import os
import allure_pytest

import pytest
if __name__ == '__main__':
    #./allure-results测试数据存放位置
    #../test_cases/test_case_search_pytest.py测试用例路径
    #-s输出日志信息，-v详细日志信息，-rA简单日志信息
    pytest.main(['-s', '../test_cases/', '--alluredir','./allure-results'])
    #生成测试报告，将测试数据生成测试报告，./reports测试报告路径，--clean覆盖测试报告
    os.system('allure generate ./allure-results -o ./reports --clean')