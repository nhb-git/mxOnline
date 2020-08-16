#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：8/15/2020  11:09 PM 
# 文件名称   ：forms.py
from django import forms
from captcha.fields import CaptchaField

from apps.utils.redis_obj import redis_obj
from apps.users.models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(min_length=2, required=True)
    password = forms.CharField(min_length=2, required=True)


class DynamicLoginForm(forms.Form):
    mobile = forms.CharField(max_length=11, min_length=11)
    captcha = CaptchaField()


class DynamicLoginPostForm(forms.Form):
    mobile = forms.CharField(max_length=11, min_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis_obj()
        if code != r.get(str(mobile)):
            raise forms.ValidationError('验证码不正确')
        return self.cleaned_data


class RegisterGetForm(forms.Form):
    """注册get表单"""
    captcha = CaptchaField()


class RegisterPostForm(forms.Form):
    """注册post表单"""
    mobile = forms.CharField(max_length=11, min_length=11)
    code = forms.CharField(required=True, min_length=4, max_length=4)
    password = forms.CharField(required=True)

    def clean_mobile(self):
        mobile = self.data.get('mobile')
        user = UserProfile.objects.filter(mobile=mobile)
        if user:
            raise forms.ValidationError('用户已存在，请更换手机号码')
        else:
            return mobile

    def clean_code(self):
        mobile = self.data.get('mobile')
        code = self.data.get('code')
        r = redis_obj()
        redis_code = r.get(str(mobile))
        if code == redis_code:
            return code
        else:
            raise forms.ValidationError('验证码错误')

