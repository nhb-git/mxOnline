#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/15/2020  6:23 PM 
# 文件名称   ：adminx.py
import xadmin

from apps.organizations.models import Teacher, CourseOrg, City


class TeacherAdmin:
    list_display = ['id', 'name', 'work_company', 'points']
    search_fields = ['name', 'work_company', 'points']
    list_filter = ['name', 'work_company', 'add_time', 'points']
    list_editable = ['name', 'work_company', 'points']


class CourseOrgAdmin:
    list_display = ['id', 'name', 'category', 'city']
    search_fields = ['name', 'desc', 'city']
    list_filter = ['name', 'desc', 'add_time', 'city']
    list_editable = ['name', 'desc', 'city']


class CityAdmin:
    list_display = ['id', 'name', 'desc']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']
    list_editable = ['name', 'desc']


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(City, CityAdmin)
