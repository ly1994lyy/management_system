from django.db import models


# Create your models here.
class Stu(models.Model):
    sex_choices = (
        ('male', '男'),
        ('female', '女'),
    )
    class_choices = (
        ('1', '高一'),
        ('2', '高二'),
        ('3', '高三'),
    )
    name = models.CharField('姓名', max_length=30)
    age = models.IntegerField('年龄')
    sex = models.CharField('性别', max_length=10, choices=sex_choices, default='male')
    classes = models.CharField('年级', max_length=10, choices=class_choices, default='1')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Score(models.Model):
    student_name = models.OneToOneField(Stu, on_delete=models.CASCADE, verbose_name='学生姓名')
    chinese_score = models.PositiveIntegerField('语文成绩')
    math_score = models.PositiveIntegerField('数学成绩')
    english_score = models.PositiveIntegerField('英语成绩')

    class Meta:
        verbose_name = '成绩管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s' % self.student_name
