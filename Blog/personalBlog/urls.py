from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index, name='blog'),
    url(r'^register/$', register),
    url(r'^register_check/$', register_check),
    url(r'^login_check/$', login_check),
    url(r'^article/$', blog_page),
    url(r'^comment_send/$', comment_send),
]
