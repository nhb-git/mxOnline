from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime


# BaseModel放入users中可以防止循环引用
class BaseModel(models.Model):
    """公共基础表"""
    # add_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)

    class Meta:
        abstract = True


class UserProfile(AbstractUser):
    """用户表"""
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女')
    )
    nick_name = models.CharField(verbose_name='昵称', max_length=50, default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(verbose_name='性别', choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(verbose_name='地址', max_length=100, default='')
    mobile = models.CharField(verbose_name='手机号码', max_length=11)
    image = models.ImageField(verbose_name='头像', upload_to='head_image/%Y/%m', default='default.jpg')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
