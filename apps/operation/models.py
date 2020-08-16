from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
# from apps.courses.models import Course

UserProfile = get_user_model()


class UserAsk(BaseModel):
    """用户咨询表"""
    name = models.CharField(verbose_name='用户名', max_length=20)
    mobile = models.CharField(verbose_name='手机号码', max_length=11)
    course_name = models.CharField(verbose_name='咨询课程名称', max_length=50)

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{name}_{course}({mobile})'.format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    """课程评论表"""
    user = models.ForeignKey(verbose_name='用户', to='users.UserProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(verbose_name='课程', to='courses.Course', on_delete=models.CASCADE)
    comments = models.CharField(verbose_name='评论', max_length=200)

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(BaseModel):
    """用户收藏表"""
    fav_id = models.IntegerField(verbose_name='数据id')
    fav_type = models.IntegerField(
        verbose_name='收藏类型', choices=((1, '课程'), (2, '课程机构'), (3, '讲师')),
        default=1
    )
    user = models.ForeignKey(verbose_name='用户', to='users.UserProfile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{user}_{fav_id}'.format(user=self.user, fav_id=self.fav_id)


class UserMessage(BaseModel):
    """用户消息"""
    message = models.CharField(verbose_name='用户消息', max_length=200)
    has_read = models.BooleanField(verbose_name='是否已读', default=False)
    user = models.ForeignKey(verbose_name='用户', to='users.UserProfile', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user


class UserCourse(BaseModel):
    """用户课程"""
    user = models.ForeignKey(verbose_name='用户', to='users.UserProfile', on_delete=models.CASCADE)
    course = models.ForeignKey(verbose_name='课程', to='courses.Course', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course
