from django.db import models
import django.utils.timezone as timezone


# Create your models here.

class UserInfo(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=15, unique=True, null=True)
    pwd = models.CharField(max_length=80)


class BlogContent(models.Model):
    title = models.CharField(max_length=40)
    text = models.TextField()
    create_date = models.DateTimeField('创建时间', default=timezone.now)
    update_date = models.DateTimeField('更新时间', auto_now=True)
    look_num = models.IntegerField(default=0)
    comment_num = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)


class BlogComment(models.Model):
    comment = models.CharField(max_length=200)
    comment_time = models.DateTimeField('评论时间', auto_now=True)
    blog_comment = models.ForeignKey('BlogContent')
    user_comment = models.ForeignKey('UserInfo')
    is_delete = models.BooleanField(default=False)
