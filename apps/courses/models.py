from django.db import models

from apps.users.models import BaseModel

from apps.organizations.models import Teacher


class Course(BaseModel):
    """课程表"""
    name = models.CharField(verbose_name='课程名称', max_length=50)
    desc = models.CharField(verbose_name='课程描述', max_length=300)
    learn_times = models.IntegerField(verbose_name='课程时长(分钟数)', default=0)
    degree = models.CharField(
        verbose_name='课程难度', max_length=5, choices=(('cj', '初级'), ('zj', '中级'), ('gj', '高级'))
    )
    students = models.IntegerField(verbose_name='学习人数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏人数', default=0)
    click_nums = models.IntegerField(verbose_name='点击人数', default=0)
    category = models.CharField(verbose_name='课程类别', max_length=30, default='后端开发')
    tag = models.CharField(verbose_name='课程标签', max_length=30, default='')
    youneed_know = models.CharField(verbose_name='课程须知', max_length=300, default='')
    teacher_tell = models.CharField(verbose_name='老师告诉你', max_length=300, default='')
    detail = models.TextField(verbose_name='课程详情')
    image = models.ImageField(verbose_name='课程图片', upload_to='courses/%Y/%m', max_length=100)
    teacher = models.ForeignKey(verbose_name='课程老师', to='organizations.Teacher', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lesson(BaseModel):
    """章节表"""
    course = models.ForeignKey(
        verbose_name='课程', to='Course', on_delete=models.CASCADE
    )   # 课程相关数据被删除后章节信息也删除
    name = models.CharField(verbose_name='章节名称', max_length=50)
    learn_times = models.IntegerField(verbose_name='章节时长(分钟数)', default=0)

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    """视频表"""
    lesson = models.ForeignKey(verbose_name='章节', to='Lesson', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='视频名称', max_length=50)
    learn_times = models.IntegerField(verbose_name='视频时长(分钟数)', default=0)
    url = models.CharField(verbose_name='视频地址', max_length=200)

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        self.name


class CourseResource(BaseModel):
    """课程资源表"""
    name = models.CharField(verbose_name='课程资源名称', max_length=50)
    course = models.ForeignKey(verbose_name='课程', to='Course', on_delete=models.CASCADE)
    file = models.FileField(verbose_name='课程资源文件下载地址', upload_to='course/resources/%Y/%m', max_length=200)

    class Meta:
        verbose_name = '课程资源信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
