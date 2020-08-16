from django.shortcuts import render, reverse
from django.views.generic.base import View
from django.contrib import auth
from django.http import HttpResponseRedirect, JsonResponse

from apps.users.forms import (
    LoginForm, DynamicLoginForm, DynamicLoginPostForm, RegisterGetForm, RegisterPostForm
)
from apps.utils.yunpian import send_single_sms
from apps.utils.random_str import generate_random
from apps.utils.redis_obj import redis_obj
from apps.users.models import UserProfile


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return HttpResponseRedirect(reverse('index'))


class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('index'))
        login_form = DynamicLoginForm()
        return render(request, 'login.html', {'login_form': login_form})

    def post(self, request, *args, **kwargs):
        login_form = LoginForm(request.POST)
        # user_name = request.POST.get('username', '')
        # password = request.POST.get('password', '')
        if login_form.is_valid():
            # 用户通过用户名和密码查询用户是否存在
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(username=user_name, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'login.html', {'msg': '请输入正确的用户名或密码', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class SendSmsView(View):
    def post(self, request, *args, **kwargs):
        send_sms_form = DynamicLoginForm(request.POST)
        re_dict = dict()
        if send_sms_form.is_valid():
            mobile = send_sms_form.cleaned_data['mobile']
            # 随机生成数字验证码
            code = generate_random(4, 0)
            re_json = send_single_sms(code, mobile)
            if re_json['code'] == 0:
                re_dict['status'] = 'success'
                r_obj = redis_obj()
                r_obj.setex(str(mobile), 60*5, code)
            else:
                re_dict['msg'] = re_json['msg']
        else:
            for key, error in send_sms_form.errors.items():
                re_dict[key] = error[0]
        return JsonResponse(re_dict)


class DynamicLoginView(View):
    def post(self, request, *args, **kwargs):
        dynamic_login = DynamicLoginPostForm(request.POST)
        if dynamic_login.is_valid():
            # 没有注册账号依然可以登录
            mobile = dynamic_login.cleaned_data['mobile']
            existed_user = UserProfile.objects.filter(mobile=mobile)
            if existed_user:
                user = existed_user[0]
            else:
                # 新建一个用户
                user = UserProfile(username=mobile)
                password = generate_random(10, 2)
                user.set_password(password)
                user.mobile = mobile
                user.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            d_login_form = DynamicLoginForm()
            return render(
                request, 'login.html', {
                    'dynamic_login': dynamic_login, 'd_form': d_login_form
                }
            )


class RegisterView(View):
    """
    注册类
    """
    def get(self, request, *args, **kwargs):
        register_get_form = RegisterGetForm()
        return render(request, 'register.html', {'register_get_form': register_get_form})

    def post(self, request, *args, **kwargs):
        register_post_form = RegisterPostForm(request.POST)
        if register_post_form.is_valid():
            # 没有注册账号则注册
            mobile = register_post_form.cleaned_data['mobile']
            password = register_post_form.cleaned_data['password']
            # 新建一个用户
            user = UserProfile(username=mobile)
            user.set_password(password)
            user.mobile = mobile
            user.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            register_get_form = RegisterGetForm()
            return render(
                request, 'register.html', {
                    'register_post_form': register_post_form, 'register_get_form': register_get_form
                }
            )
