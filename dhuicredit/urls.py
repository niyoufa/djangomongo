#coding=utf-8

from django.conf.urls import url, include
from dhuicredit import views

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9a-z]+)/$', views.UserDetail.as_view()),
]