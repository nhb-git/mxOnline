#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/16/2020  1:37 AM 
# 文件名称   ：redis_obj.py
import redis
from MxOnline.settings import REDIS_HOST, REDIS_PORT


def redis_obj(host=REDIS_HOST, port=REDIS_PORT):
    r = redis.Redis(host, port, db=0, charset='utf8', decode_responses=True)
    return r
