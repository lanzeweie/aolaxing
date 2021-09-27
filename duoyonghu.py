# -*- coding:utf-8 -*- 

from os import close
from selenium import webdriver
import time
import json
import os

#头信息
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--incognito')
#chromeOptions.add_argument('--headless')
#chromeOptions.add_argument('--no-sandbox')
chromeOptions.add_argument('--disable-javascript')
chromeOptions.add_argument('user-agent="Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"')
aola = webdriver.Chrome(chrome_options=chromeOptions)

#进入网页+登录
weizhicookies = os.path.dirname(os.path.abspath(__file__))
shu = 0
for s in range(6):
    aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
    
    aola.delete_all_cookies()
    weicook = weizhicookies+'/cookies'+str(shu)+'.txt'
    shu += 1
    #print(weicook)

    with open(weicook,'r') as f:
        cookies_list = json.load(f)
        for cookie in cookies_list:
            aola.add_cookie(cookie)

    aola.refresh()

    if aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text == '登录有礼':
        print('账号 cookies不正确或过期，请重新获取')
        continue

    user = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text
    print('账号 '+user+' 开始任务')

    print(aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text)

    time.sleep(0.3)
    aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.3)

#开始任务
    #每日签到
    try:
        #print('签到')
        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[1]/div[3]').click()
        time.sleep(0.5)
        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[5]/div[2]/div[7]/div').click()
        time.sleep(0.75)
    except:
        pass
    time.sleep(0.75)
    #答题
    #从上至下依次点击
    dati = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[2]/div[3]').text
    if dati == '已完成':
        pass
    else:
        try:
            print('答题')
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

            time.sleep(1.5)
            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[9]/div[2]/div[7]/div').click()
        except:
            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[9]/div[2]/div[7]/div').click()
    time.sleep(0.75)

    #看广告(1) 签到拿潘多拉角色立牌 
    guanggao1 = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[4]/div[3]').text
    if guanggao1 == '已完成':
        pass
    elif guanggao1 != '已完成':
        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[4]/div[3]').click()
        try:
            time.sleep(0.5)
            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[10]/div[2]/div[5]').click()
        except:
            #aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[4]/div[3]').click()
            time.sleep(1)
            #判断是什么任务
            url_now = (aola.current_url)
            if url_now == 'http://www.100bt.com/m/creditMall/?gameId=2#task':
                try:
                    tiaozhuan = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[4]/div[3]').text
                    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[4]/div[3]').click()
                except:
                    pass
                print('开始潘多拉循环')
                while True:
                    try:
                        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[10]/div[2]/div[7]/div').text
                        print('任务已满或者是预约任务')
                        time.sleep(0.25)
                        try:    
                            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[10]/div[2]/div[7]/div').click()
                        except:
                            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[14]/div/div[2]/div[1]').click()
                        break
                    except:
                        pass
                    try:
                        quxiao = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').text
                    except:
                        time.sleep(2)
                        continue
                    if quxiao == '取 消':
                        print('潘多拉主要元素获取成功')
                        time.sleep(33)
                        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').click()
                        break
            else:
                time.sleep(1)
                aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
                time.sleep(0.75)
                aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    time.sleep(0.75)

    #看广告1.1 不是每个账号都有
    try:
        guanggao1_1 = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[3]/div[3]').text
        if guanggao1_1 == '已完成':
            pass
        elif guanggao1_1 == '去完成':
            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[3]/div[3]').click()
            try:
                aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[14]/div/div[2]/div[1]').text
                time.sleep(0.5)
                aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[14]/div/div[2]/div[1]').click()
            except:
                #判断是什么任务
                time.sleep(1)
                url_now = (aola.current_url)
                if url_now == 'http://www.100bt.com/m/creditMall/?gameId=2#task':
                    print('开始看广告1.1循环')
                    while True:
                        print('成功进入广告1.1')
                        try:
                            quxiao_1 = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').text
                        except:
                            time.sleep(2)
                            continue
                        if quxiao_1 == '取 消':
                            print('广告1.1主要元素获取成功')
                            time.sleep(33)
                            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').click()
                            break
                else:
                    time.sleep(1)
                    aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
                    time.sleep(0.75)
                    aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    except:
        pass

    time.sleep(0.95)
    #第五个选项  因为出现过咨询与广告 所以添加判断
    guanggao2 = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[5]/div[3]').text
    if guanggao2 == '已完成':
        pass
    elif guanggao2 == '去完成':
        time.sleep(1)
        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[5]/div[3]').click()
        time.sleep(1)
        #判断是什么任务
        url_now = (aola.current_url)
        if url_now == 'http://www.100bt.com/m/creditMall/?gameId=2#task':
            print('开始第五个选项循环')
            while True:
                try:
                    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[10]/div[2]/div[7]/div').text
                    print('任务已满结束')
                    time.sleep(0.25)
                    try:    
                        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[10]/div[2]/div[7]/div').click()
                    except:
                        aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[14]/div/div[2]/div[1]').click()
                    break
                except:
                    pass
                print('成功进入第五个选项')
                try:
                    quxiao = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').text
                except:
                    time.sleep(2)
                    continue
                if quxiao == '取 消':
                    print('第五个选项主要元素获取成功')
                    time.sleep(33)
                    aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[16]/div[2]/div[8]/div').click()
                    break
        else:
            pass
            time.sleep(1)
            aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')
            time.sleep(0.75)
            aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.75)

    aola.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(0.85)
    #最后一项结束任务
    #print('最后一项看咨询')
    try:
        zixun = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[6]/div[3]').text
        if zixun == '已完成':
            pass
        else:
            aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[3]/div/div[2]/div[6]/div[3]').click()
    except:
        pass
    time.sleep(1)

    #重新打开链接获取当前积分信息 并发传递给钉钉
    #print('发送钉钉')
    aola.get('http://www.100bt.com/m/creditMall/?gameId=2#task')

    zhanghao_text = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[1]').text
    jifen_text = aola.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div[2]/span[2]').text

    #aola.quit()

    print(zhanghao_text)
    print(jifen_text)

