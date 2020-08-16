#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/15/2020  7:00 PM 
# 文件名称   ：adminx.py
import xadmin

from apps.operation.models import UserAsk, UserCourse, UserFavorite, UserMessage, CourseComments


class UserAskAdmin:
    pass


class UserFavoriteAdmin:
    pass


class UserCourseAdmin:
    pass


class UserMessageAdmin:
    pass


class CourseCommentsAdmin:
    pass


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
