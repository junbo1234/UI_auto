'''
pytest规则：
1、测试文件以test_开头，或者以_test结尾
2、测试类以Test开头，并且不能带有init方法
3、测试函数以test_开头
4、以上3点可以通过pytest.ini文件修改配置
5、断言使用assert
'''
'''
运行：
1、main方法
2、终端运行
3、显示所有执行结果-s ,显示详细结果-v
'''
'''
        @pytest.mark.run(order=1)  #执行顺序
        @pytest.mark.smoke #冒烟测试,需要在pytest.ini文件补充
        @pytest.mark.skip('跳过') #跳过该条
        @pytest.mark.skipif(num<11, reason='跳过测试')
'''
import pytest

# def setup_module():
#     print('作用与整个模块')
# def teardown_module():
#     print('作用与整个模块')


class Testcase:
    num=10
    def setup_class(self):
        print('类的前置条件')
    def teardown_class(self):
        print('类的后置条件')

    def setup(self):
        print('方法执行前')
    def teardown(self):
        print('方法执行后处理')

    @pytest.mark.run(order=2)
    def test_01(self):
        print('用例1 case')
        assert 1==1
    @pytest.mark.run(order=1)  #执行顺序
    @pytest.mark.smoke #冒烟测试,需要在pytest.ini文件补充
   # @pytest.mark.skip('跳过') #跳过该条
    @pytest.mark.skipif(num<11, reason='跳过测试')
    def test_02(self):
        print('用例2 case')
        assert 2==2
    @pytest.mark.run(order=3)
    def test_03(self):
        print('用例3 case')
        assert 2==2

if __name__ == '__main__':
    pytest.main('-s', '-v', 'py_test.py')