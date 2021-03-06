# Generated by Django 2.0.6 on 2018-06-20 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('sex', models.CharField(choices=[('male', '男'), ('female', '男')], default='male', max_length=5, verbose_name='性别')),
                ('classes', models.CharField(choices=[('1', '高一'), ('2', '高二'), ('3', '高三')], default='1', max_length=5, verbose_name='年级')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
            },
        ),
    ]
