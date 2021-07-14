# -*- coding:utf-8 -*- 
#引入selenium package, 建立webdriver对象
from os import close
from selenium import webdriver
import time
import json

#头信息
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--incognito')
chromeOptions.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"')
aola = webdriver.Chrome(chrome_options=chromeOptions)

#进入网页+登录
aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
aola.delete_all_cookies()

with open('cookies4.txt','r') as f:
    cookies_list = json.load(f)
    for cookie in cookies_list:
        aola.add_cookie(cookie)
aola.refresh()
time.sleep(0.3)
aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(0.3)

#开始任务
#每日签到
try:
    #print(1)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/div[3]').click()
    time.sleep(0.5)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[5]/div[2]/div[7]/div').click()
except:
    pass
time.sleep(1)
#答题
#从上至下依次点击
try:
    #print(2)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[2]/div[3]').click()
    time.sleep(0.4)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[8]/div[2]/div[7]/div[1]').click()
    time.sleep(0.2)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[8]/div[2]/div[8]/div').click()

    time.sleep(0.3)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[8]/div[2]/div[7]/div[2]').click()
    time.sleep(0.4)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[8]/div[2]/div[8]/div').click()
    time.sleep(0.3)

    time.sleep(0.4)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[8]/div[2]/div[7]/div[3]').click()
    time.sleep(0.2)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[8]/div[2]/div[8]/div').click()

    time.sleep(0.5)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[9]/div[2]/div[5]').click()
except:
    pass
time.sleep(0.75)
#看广告(1) 签到拿潘多拉角色立牌
if aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[4]/div[3]').text == '已完成':
    print('yes')
    pass
else:
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[4]/div[3]').click()
    time.sleep(32)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').click()
    time.sleep(2)

time.sleep(0.75)
#看广告(2) 寻找最初的伙伴
if aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[5]/div[3]').text == '已完成':
    pass
else:
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[5]/div[3]').click()
    time.sleep(32)
    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').click()
    time.sleep(2)

time.sleep(0.75)
#最后一项结束任务
aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[6]/div[3]').click()
time.sleep(0.75)

#print(5)
aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')

zhanghao_text = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text
jifen_text = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[2]').text

print(zhanghao_text)
print(jifen_text)