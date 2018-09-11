# Generated by Django 2.0.5 on 2018-09-09 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('math_score', models.CharField(max_length=20, verbose_name='数学成绩')),
                ('english_score', models.CharField(max_length=20, verbose_name='英语成绩')),
                ('chinese_score', models.CharField(max_length=20, verbose_name='语文成绩')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Students', verbose_name='学生')),
            ],
            options={
                'verbose_name': '学生成绩',
                'verbose_name_plural': '学生成绩',
            },
        ),
    ]
