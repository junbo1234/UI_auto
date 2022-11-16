'''
读取yaml数据
'''
import yaml

def loadyml(filename):
    files = open(filename, 'r', encoding='utf-8')
    #读取
    data = yaml.load(files, Loader=yaml.FullLoader)
    return data

# a = loadyml('../data/user.yaml')
# print(a)