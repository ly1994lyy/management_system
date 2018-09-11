from django.db import models
from django.urls import reverse
# Create your models here.


class Students(models.Model):
    classes_choices = (
        ('1', '初一'),
        ('2', '初二'),
        ('3', '初三'),
    )
    sex_choices = (
        ('1', '男'),
        ('2', '女'),
    )
    name = models.CharField('学生姓名', max_length=20)
    age = models.IntegerField('学生年龄')
    classes = models.CharField('年级', max_length=30, choices=classes_choices, default='1')
    sex = models.CharField('性别', max_length=20, choices=sex_choices, default='1')

    class Meta:
        verbose_name = '学生列表'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('student_list')

    def __str__(self):
        return self.name