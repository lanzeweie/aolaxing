# -*- coding:utf-8 -*- 
from selenium import webdriver
import time
import json


driver = webdriver.Chrome()
driver.get('http://www.100bt.com/m/creditMall/?gameId=2#home')

time.sleep(1)

while True:
    if driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text == '登录有礼':
        pass
    else:
        break
   
cookie = json.dumps(driver.get_cookies())
driver.close()
cookie_json = json.loads(cookie)
ID = ""
for shu in range(len(cookie_json)):
    name = cookie_json[shu]['name']
    value = cookie_json[shu]['value']
    ID += (f"{name}={value}; ")
print(ID)
