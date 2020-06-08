from django.db import models
from personalBlog.models import UserInfo


# Create your models here.
class TodoItem(models.Model):
    todo_content = models.CharField(max_length=256)
    todo_user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
