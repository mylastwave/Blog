# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-06-07 10:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personalBlog', '0002_auto_20200607_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='user_comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='personalBlog.UserInfo'),
            preserve_default=False,
        ),
    ]
