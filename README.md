#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: QLaolastart.py(奥拉星积分商店签到)
Author: Hennessey
Date: 2023/7/3 11:40
cron: 30 6 * * *
new Env('奥拉星积分商店签到');
Update: 2023/7/3 上线青龙
"""

import requests,json,time,os,random,sys
#from DingBotSend import Dingbot
weizhi = os.path.dirname(os.path.abspath(__file__))

class aola():
    def set(Cookie):
        global hand
        uatxt = open(weizhi+'/ua.txt',encoding='UTF-8')
        ua_lin = uatxt.readlines()
        urlits = []
        for UA in ua_lin:
            temp=UA.replace('\n','')
            urlits.append(temp)
        UAt = random.choice(urlits)
        hand = {
        "Host": "service.100bt.com",
        "Proxy-Connection": "keep-alive",
        "User-Agent": UAt,
        "Accept": "*/*",
        "Referer": "http://www.100bt.com/",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cookie":Cookie
        }

    def user():
        url = "http://service.100bt.com/creditmall/my/user_info.jsonp"
        user = requests.get(url,headers=hand)
        user_json = json.loads(user.text)
        user_data = user_json['jsonResult']['data']
        try:
            credit = user_data['credit']
            creditHistory = user_data['creditHistory']
            phoneNum = user_data['phoneNum']
            signInTotal = user_data['signInTotal']
            jsonResultname = user_data['name']
        except:
            credit = "errow"
            return credit,None,None,None,None
        print(f"用户：{phoneNum}\n当前积分：{credit} 总共获得积分：{creditHistory}\n总签到：{signInTotal} 天")
        return credit,creditHistory,phoneNum,signInTotal,jsonResultname
        
    def task():
        url = "http://service.100bt.com/creditmall/activity/daily_task_list.jsonp?gameId=2&_=1643437206026"
        task = requests.get(url,headers=hand)
        task_json = json.loads(task.text)
        task_data = task_json['jsonResult']['data']
        task_len = len(task_data)
        for shu in range(task_len):
            name = task_data[shu]['name']
            status_desc = task_data[shu]['status_desc']
            taskID = task_data[shu]['taskID']
            print(f"\n任务：{name} 状态：{status_desc}")
            if status_desc == "已完成":
                continue
            if status_desc == "未完成":
                print(f"开始任务：{name}")
                zhixing = aola.practise(taskID)
                print(f"返回状态：{zhixing}")
                time.sleep(2.5)
        task_len1,task_surr = aola.task_jian()
        return task_len1,task_surr
        
    def task_jian():
        url = "http://service.100bt.com/creditmall/activity/daily_task_list.jsonp?gameId=2&_=1643437206026"
        task = requests.get(url,headers=hand)
        task_json = json.loads(task.text)
        task_data = task_json['jsonResult']['data']
        task_len = len(task_data)
        task_surr = 0
        for shu in range(task_len):
            status_desc = task_data[shu]['status_desc']
            if status_desc == "已完成":
                task_surr+=1
        print(f"今日任务总数：{task_len},完成数：{task_surr}")
        return task_len,task_surr

    def practise(taskID):
        url = f"http://service.100bt.com/creditmall/activity/do_task.jsonp?taskId={taskID}&gameId=2&_=1643440166690"
        task = requests.get(url,headers=hand)
        task_json = json.loads(task.text)
        message = task_json['jsonResult']['message']
        return message

    def start(Cookie):
        print("首次获得用户信息")
        credit,creditHistory,phoneNum,signInTotal,jsonResultname  = aola.user()
        if credit == "errow":
            return "Cookie失效"
        task_len,task_surr = aola.task()
        print("再次获得用户信息")
        now_credit,now_creditHistory,now_phoneNum,now_signInTotal,jsonResultname = aola.user()
        jifen = now_credit - credit
        Send = (f"\n\n【用户】🆔{now_phoneNum}\n【今日总任务数】{task_len}，成功数量：{task_surr} 个\n【本次获得积分】{jifen}\n【当前积分】{now_credit}\n【总共签到】{now_signInTotal} 天")
        return Send

    def Cookie():
        CookieJDs = []
        if 'AOLA_COOKIE' in os.environ:
            if '&' in os.environ['AOLA_COOKIE']:
                CookieJDs = os.environ['AOLA_COOKIE'].split('&')
            elif '\n' in os.environ['AOLA_COOKIE']:
                CookieJDs = os.environ['AOLA_COOKIE'].split('\n')
            else:
                CookieJDs = [os.environ['AOLA_COOKIE']]
        CookieJDs = list(set(filter(None, CookieJDs)))
        #print(f'\n====================共{len(CookieJDs)}个奥拉星账户Cookie=================\n')
        
        return CookieJDs

    def zhu():
        Cookie_list_H = aola.Cookie()
        Cookie_list_Len = len(Cookie_list_H)
        print(f"用户数量：{Cookie_list_Len}")
        #Cookie_list_Len 有多少个元素就执行多少次
        siji = 0
        for Cookie_list in Cookie_list_H:
            siji = 1
            aola.set(Cookie_list)
            Send_zhong = (aola.start(Cookie_list))
            if Send_zhong == "Cookie失效":
                print("账户：",Cookie_list,"\nCookie失效")
                break
        if siji >= 1:
            pass
        else:
            print("====================未检测到用户Cookie,结束运行====================")
            return "没有检测到可以使用的用户Cookie"
        Send_tou = ("奥拉星积分商城活动")
        Send_wei = ("\n\n活动地址\nhttp://www.100bt.com/m/creditMall/?gameId=2#task\n仅供个人使用,不构成任何商业性质")
        Send = Send_tou+Send_zhong+Send_wei
        #Dingbot.Send(Send)
        return Send
            
    # 加载通知服务
    def load_send():
        cur_path = os.path.abspath(os.path.dirname(__file__))
        sys.path.append(cur_path)
        if os.path.exists(cur_path + "/sendNotify.py"):
            try:
                from sendNotify import send
                return send
            except Exception as e:
                print(f"加载通知服务失败：{e}")
                return None
        else:
            print("加载通知服务失败")
            return None

if __name__ == "__main__":
    #from dotenv import load_dotenv
    #load_dotenv()
    import datetime
    now_riqi = datetime.datetime.now().strftime('[%Y/%m/%d, %H:%M:%S]')
    print(f"==================程序执行- 北京时间(UTC+8)：{now_riqi} PM=====================\n")
    contents = aola.zhu()
    send_notify = aola.load_send()
    if send_notify:
        send_notify("奥拉星活动助手",contents)
    
    
