from django.shortcuts import render, HttpResponse, redirect, reverse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import *


def register(request):
    return render(request, 'personalBlog/register.html')


@csrf_exempt
def register_check(request):
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    # 验证邮箱是否已经被注册过
    is_exist_email = UserInfo.objects.filter(email=email)
    if is_exist_email:
        return HttpResponse('EXIST')
    user = UserInfo()
    user.email = email
    pwd = make_password(pwd)
    user.pwd = pwd
    user.save()
    response = HttpResponse('ok')
    response.set_cookie('username', email, path='/')
    return response


def index(request):
    data = []
    # 对查询结果进行排序，让id大的在前面，渲染到博客的时候，新发布的就会在前面
    blogs = BlogContent.objects.filter(is_delete=False).order_by('-id')
    # blogs = list(blogs)
    # print(blogs)
    for blog in blogs:
        blog_id = blog.id
        title = blog.title
        date = blog.create_date
        look_num = blog.look_num
        comment_num = blog.comment_num
        content = blog.text[:80] + '……'
        data.append({
            'id': blog_id,
            'title': title,
            'date': date,
            'look_num': look_num,
            'comment_num': comment_num,
            'content': content
        })
    return render(request, 'personalBlog/blog.html', {'blogs': data})


def blog_page(request):
    blog_id = request.GET.get('id')
    blog = BlogContent.objects.get(id=blog_id)
    title = blog.title
    date = blog.create_date
    look_num = blog.look_num
    comment_num = blog.comment_num
    content = blog.text
    comments = blog.blogcomment_set.all()
    comment_list = []
    for comment in comments:
        # 评论时间
        comment_date = comment.comment_time
        # 评论的用户名称
        comment_user = comment.user_comment
        user_name = comment_user.email
        # 评论内容
        comment_text = comment.comment
        # 插入评论列表
        comment_list.append({'date': comment_date, 'username': user_name, 'comment': comment_text})
    # 倒序列表，让时间上先发的评论在列表越后
    comment_list.reverse()
    blog.look_num += 1
    blog.save()
    return render(request, 'personalBlog/article.html', {
        'title': title,
        'date': date,
        'look_num': look_num + 1,
        'comment_num': comment_num,
        'content': content,
        'comment_list': comment_list,
        'blog_id': blog_id
    })


@csrf_exempt
def login_check(request):
    email = request.POST.get('email')
    pwd = request.POST.get('pwd')
    user_list = UserInfo.objects.filter(email=email)
    if not user_list:
        return HttpResponse('email_non')
    user = user_list[0]
    if not check_password(pwd, user.pwd):
        return HttpResponse('wrong')
    response = HttpResponse('ok')
    response.set_cookie('username', email, path='/')
    return response


def comment_send(request):
    email = request.GET.get('username')
    comment_text = request.GET.get('comment')
    user = UserInfo.objects.get(email=email)
    blog_id = request.GET.get('article_id')
    blog = BlogContent.objects.get(id=blog_id)
    comment = BlogComment()
    comment.comment = comment_text
    comment.user_comment = user
    comment.blog_comment = blog
    comment.save()
    blog.comment_num += 1
    blog.save()
    return HttpResponse('ok')
