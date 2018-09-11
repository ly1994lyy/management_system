from django.db import models
from students.models import Students
# Create your models here.


class Score(models.Model):
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE, verbose_name='学生')
    math_score = models.CharField('数学成绩', max_length=20)
    english_score = models.CharField('英语成绩', max_length=20)
    chinese_score = models.CharField('语文成绩', max_length=20)

    def __str__(self):
        return self.student_name.name

    class Meta:
        verbose_name = '学生成绩'
        verbose_name_plural = verbose_name