#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
#python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse
#暂存信息

class Dingbot():
    def Send(Send):
        timestamp = str(round(time.time() * 1000))
        secret = ''
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        url=''.format(timestamp, sign)
        headers={
        'Content-Type':'application/json'
        }
        json={"msgtype": "text",
            "text": {
                "content":Send
            },
            "at": {
                "atDingtalkIds": [
                    
                ],
                "isAtAll": False
            }
        }
        resp=requests.post(url=url,headers=headers,json=json)

if __name__ == "__main__":
    send = "123"
    Dingbot.Send(send)
