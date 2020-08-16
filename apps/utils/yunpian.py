#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/16/2020  12:19 AM 
# 文件名称   ：yunpian.py
import requests
import json
from MxOnline.settings import YP_APIKEY


def send_single_sms(code, mobile, apikey=YP_APIKEY):
    url = 'https://sms.yunpian.com/v2/sms/single_send.json'
    text = '【牛海保】您的验证码是{}'.format(code)

    res = requests.post(url, data={
        'apikey': apikey,
        'mobile': mobile,
        'text': text}
    )
    re_json = json.loads(res.text)
    return re_json
    # return {'code': 0}
