from selenium import webdriver
import yaml


file = open('../data/data1.yaml', 'r', encoding='utf-8')
data = yaml.load(file, Loader=yaml.FullLoader)

print(type(data))

print(data)
