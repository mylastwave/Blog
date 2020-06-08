from django.contrib import admin
from .models import *


class BlogContentAdmin(admin.ModelAdmin):
    list_display = ['title']


class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['blog_comment']


admin.site.register(BlogContent, BlogContentAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
