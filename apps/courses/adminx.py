#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/15/2020  6:20 PM 
# 文件名称   ：adminx.py
import xadmin

from apps.courses.models import Course, Lesson, CourseResource, Video


class GlobalSettings:
    site_title = '慕课后台管理系统'
    site_footer = '慕课网'
    # menu_style = 'accordion'


class BaseSettings:
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ['id', 'name', 'desc', 'learn_times', 'degree', 'teacher']
    search_fields = ['name', 'desc', 'degree', 'detail']
    list_filter = ['name', 'teacher__name', 'desc', 'add_time', 'degree']
    list_editable = ['name', 'desc', 'degree']


class LessonAdmin:
    pass


class VideoAdmin:
    pass


class CourseResourceAdmin:
    pass


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
# 定义xadmin后台的全局信息
xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
