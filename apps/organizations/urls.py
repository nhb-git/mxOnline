#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：9/2/2020  8:20 AM 
# 文件名称   ：urls.py
from django.urls import re_path
from apps.organizations.views import OrgView


urlpatterns = [
    re_path(r'^list/$', OrgView.as_view(), name='list'),
]
