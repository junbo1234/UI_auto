'''
DDT:Data Driver Test 数据驱动-一种设计模式
实现数据与脚本分离，便于维护与扩展
ddt 有第三方库，
'''

'''
excle读取:openpyxl
'''
import openpyxl
wk = openpyxl.load_workbook("../data/testdata.xlsx")
sheet1 = wk["sheet1"]
print(sheet1.cell(1,1).value)