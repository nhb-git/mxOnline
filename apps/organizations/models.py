from django.db import models

from apps.users.models import BaseModel


class City(BaseModel):
    """城市表"""
    name = models.CharField(verbose_name='城市', max_length=20)
    desc = models.CharField(verbose_name='描述', max_length=200)

    class Meta:
        verbose_name = '城市'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    """课程机构"""
    name = models.CharField(verbose_name='课程机构名称', max_length=50)
    desc = models.TextField(verbose_name='课程机构描述')
    tag = models.CharField(verbose_name='课程机构标签', max_length=50, default='全国知名')
    category = models.CharField(
        verbose_name='课程机构类别', max_length=10, choices=(('pxjg', '培训机构'), ('gr', '个人'), ('gx', '高校'))
    )
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    image = models.ImageField(verbose_name='课程机构图片', upload_to='org/%Y/%m', max_length=100)
    address = models.CharField(verbose_name='课程机构地址', max_length=100)
    students = models.IntegerField(verbose_name='课程机构学习人数', default=0)
    course_nums = models.IntegerField(verbose_name='课程数', default=0)
    city = models.ForeignKey(verbose_name='城市', to='City', on_delete=models.CASCADE)
    is_auth = models.BooleanField(verbose_name='是否认证', default=False)
    is_gold = models.BooleanField(verbose_name='是否金牌', default=False)

    def courses(self):
        all_courses = self.course_set.filter(is_classics=True)[:3]
        return all_courses

    class Meta:
        verbose_name = '课程机构'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    """老师表"""
    name = models.CharField(verbose_name='老师名称', max_length=20)
    work_years = models.IntegerField(verbose_name='工作年限', default=0)
    work_company = models.CharField(verbose_name='就职公司', max_length=50)
    work_position = models.CharField(verbose_name='工作职位', max_length=50)
    points = models.CharField(verbose_name='教学特点', max_length=50)
    click_nums = models.IntegerField(verbose_name='点击数', default=0)
    fav_nums = models.IntegerField(verbose_name='收藏数', default=0)
    age = models.IntegerField(verbose_name='年龄', default=18)
    image = models.ImageField(verbose_name='头像', upload_to='teacher/%Y/%m', default='', max_length=100)
    org = models.ForeignKey(verbose_name='课程机构', to='CourseOrg', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '老师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.count()
