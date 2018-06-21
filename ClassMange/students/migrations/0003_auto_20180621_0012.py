# Generated by Django 2.0.6 on 2018-06-20 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20180621_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stu',
            name='classes',
            field=models.CharField(choices=[('1', '高一'), ('2', '高二'), ('3', '高三')], default='1', max_length=10, verbose_name='年级'),
        ),
        migrations.AlterField(
            model_name='stu',
            name='sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=10, verbose_name='性别'),
        ),
    ]
