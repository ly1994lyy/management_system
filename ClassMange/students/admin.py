from django.contrib import admin
from .models import Stu, Score


# Register your models here.
@admin.register(Stu)
class StuAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'age', 'sex', 'classes')


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'chinese_score', 'math_score', 'english_score')