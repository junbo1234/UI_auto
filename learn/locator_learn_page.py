# class定位,默认找第一个属性值
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')

#class定位
# class1 = driver.find_elements(By.CLASS_NAME, 'title-content-title')[1]
# class2 = driver.find_element_by_class_name('title-content-title')[1]
#
# for i in class1:
#     print(i.text)


#tag_name定位
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# span1 = driver.find_elements(By.TAG_NAME, 'span')
# for s in span1:
#     print(s.text)

#link、partial_link，针对超链接标签
#driver.find_element(By.LINK_TEXT, '新闻').click()
# driver.find_element(By.PARTIAL_LINK_TEXT, '新').click()
# sleep(5)

#xpath定位，id、name、class、tagname；
#chrome有chropath插件，可以方便定位
#表达式写法：[@属性='属性值'] /根阶段 //所有节点 *所有元素
#driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('kexi')

#CSS定位
#driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('css') #id
# clsses = driver.find_elements(By.CSS_SELECTOR, '.title-content-title') #class
# for i in clsses:
#     print(i.text)
# span1 = driver.find_elements(By.CSS_SELECTOR, 'span') #标签
# for i in span1:
#     print(i.text)



'''
#iframe 定位，有嵌套html
driver = webdriver.Chrome()
driver.get('http://www.126.com')
iframe1 = driver.find_element(By.XPATH, '//*[@id="loginDiv"]/iframe') #通过父节点loginDiv找到子节点iframe
driver.switch_to.frame(iframe1) #切换到iframe层
driver.switch_to.default_content() #切回默认主页面
'''


'''
#切换窗口
driver.find_element(By.PARTIAL_LINK_TEXT, '新闻').click() #新增一个新闻窗口
all_handles = driver.window_handles #获取全部窗口
for handle in all_handles:
    driver.switch_to.window(handle)  # 切换到新闻窗口
    if '新闻' in driver.title:
        break
driver.find_element(By.ID, 'ww').send_keys('总书记')
'''

#复选框、下拉框
#先找到下拉框的父集aox，再通过索引找到对应选择框，也可以通过其它方式找选择框
Select(driver.find_element(By.ID, 'aox')).select_by_index('1')





sleep(5)
driver.quit()


