#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/16/2020  1:31 AM 
# 文件名称   ：redis_test.py
import redis


r = redis.Redis(host='192.168.137.131', port=6379, db=0, charset='utf8', decode_responses=True)

r.setex('name', 3, 'niu')
print(r.get('name'))
