from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import json
from .models import TodoItem
from personalBlog.models import UserInfo


# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'todolist/login.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'todolist/register.html')


def todolist(request):
    username = request.COOKIES.get('username', '')
    if username:
        response = render(request, 'todolist/todolist.html')
        return response
    else:
        return render(request, 'todolist/login.html')


def get_todos(request):
    username = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(email=username)
    todos = user.todoitem_set.all().order_by('id')
    data = []
    for todo in todos:
        data.append({'todo_id': todo.id, 'content': todo.todo_content})
    # json_data = serializers.serialize('json', data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


def create_todo(request):
    username = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(email=username)
    todo = TodoItem()
    content = request.GET.get('content')
    todo.todo_content = content
    todo.todo_user = user
    todo.save()
    todos = user.todoitem_set.all().order_by('id')
    data = []
    for todo in todos:
        data.append({'todo_id': todo.id, 'content': todo.todo_content})
    # json_data = serializers.serialize('json', data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')


def del_todo(request):
    username = request.COOKIES.get('username', '')
    user = UserInfo.objects.get(email=username)
    todo_id = request.GET.get('todo_id')
    user.todoitem_set.filter(id=todo_id).delete()
    todos = user.todoitem_set.all().order_by('id')
    data = []
    for todo in todos:
        data.append({'todo_id': todo.id, 'content': todo.todo_content})
    # json_data = serializers.serialize('json', data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
