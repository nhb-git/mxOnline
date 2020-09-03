#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：9/2/2020  8:34 PM 
# 文件名称   ：forms.py
import re
from django import forms
from apps.operation.models import UserAsk


class AddAskForm(forms.ModelForm):
    """用户咨询表单"""
    mobile = forms.CharField(min_length=11, max_length=11, required=True)

    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        """
        校验手机号码的合法性
        :return:
        """
        mobile = self.data.get('mobile')
        regex_mobile = r'^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(regex_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError('手机号码非法', code='mobile_invalid')
