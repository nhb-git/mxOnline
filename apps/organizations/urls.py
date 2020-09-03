#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：9/2/2020  8:20 AM 
# 文件名称   ：urls.py
from django.urls import re_path
from apps.organizations.views import OrgView, AddAskView, OrgHomeView, OrgTeacherView


urlpatterns = [
    re_path(r'^list/$', OrgView.as_view(), name='list'),
    re_path(r'^add_ask/$', AddAskView.as_view(), name='add_ask'),
    re_path(r'^(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='home'),
    re_path(r'^(?P<org_id>\d+)/teacher/$', OrgTeacherView.as_view(), name='teacher'),
]
