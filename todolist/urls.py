from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', todolist),
    url(r'^login/$', login),
    url(r'^register/$', register),
    url(r'^get_todos/$', get_todos),
    url(r'^create_todo/$', create_todo),
    url(r'^del_todo/$', del_todo),
]
