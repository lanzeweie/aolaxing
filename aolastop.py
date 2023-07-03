# -*- coding:utf-8 -*-
import requests,json,time,os,random
#from DingBotSend import Dingbot
weizhi = os.path.dirname(os.path.abspath(__file__))

class aola():
    def set(Cookie,user_phon):
        global hand
        global user_phons
        user_phons = user_phon
        uatxt = open(weizhi+'/ua.js',encoding='UTF-8')
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
        except:
            credit = "errow"
            return credit,None,None,None
        print(f"用户：{phoneNum}\n当前积分：{credit} 总共获得积分：{creditHistory}\n总签到：{signInTotal} 天")
        return credit,creditHistory,phoneNum,signInTotal
        
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
        try:
            message = task_json['jsonResult']['message']
        except:
            message = "NO"
        return message

    def start(Cookie,user_phon,user_updata):
        print("\n——————————————————————————————————————————")
        print("\n读取配置文件")
        aola.set(Cookie,user_phon)
        print("获取用户信息")
        credit,creditHistory,phoneNum,signInTotal = aola.user()
        if credit == "errow":
            print(f"\n\n【用户】{user_phons} 获取失败，原因：可能是当前Cookie过期\n上次Cookie更新时间：{user_updata}")
            Send = (f"\n\n【用户】{user_phons} 获取失败，原因：可能是当前Cookie过期\n上次Cookie更新时间：{user_updata}")
            return Send
        print("\n检测并执行当日任务")
        task_len,task_surr = aola.task()
        print("再次获得用户信息")
        now_credit,now_creditHistory,now_phoneNum,now_signInTotal = aola.user()
        jifen = now_credit - credit
        Send = (f"\n\n【用户】🆔{now_phoneNum}\n【今日总任务数】{task_len}，成功数量：{task_surr} 个\n【本次获得积分】{jifen}\n【当前积分】{now_credit}\n【总共签到】{now_signInTotal} 天")
        return Send

    def zhu():
        with open(f"{weizhi}/cookie.json","r",encoding='utf-8') as aola_json:
            aola_user = aola_json.read()
        user_json = json.loads(aola_user)
        user = user_json['lie']
        user_len = len(user)
        Send_zhong = ""
        print(f"用户数量：{user_len}")
        for shu in range(user_len):
            Cookie = user_json['lie'][shu]['Cookie']
            user_phon = user_json['lie'][shu]['name']
            user_updata = user_json['lie'][shu]['Updata']
            try:
                run = user_json['lie'][shu]['run']
                if run == 'no':
                    continue
            except:
                pass
            Send_zhong += aola.start(Cookie,user_phon,user_updata)
        Send_tou = ("奥拉星积分商城活动")
        Send_wei = ("\n\n活动地址\nhttp://www.100bt.com/m/creditMall/?gameId=2#task\n仅供个人使用,不构成任何商业性质")
        Send = Send_tou+Send_zhong+Send_wei
        print(Send)
        #Dingbot.Send(Send)
            
            

if __name__ == "__main__":
    import datetime
    now_riqi = datetime.datetime.now().strftime('[%Y/%m/%d, %H:%M:%S]')
    print(f"==================程序执行- 北京时间(UTC+8)：{now_riqi} PM=====================\n")
    aola.zhu()
    #在cookie.json 配置好用户 Cookie 后执行
    #Cookie 可以通过 cookie.py 获取
    #但是需要 chromedriver.exe
        
        
    
    
