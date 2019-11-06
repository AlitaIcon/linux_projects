#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/10/29 8:57
# @Author  : icon
# @File    : urls.py


from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    # path('upload/avatar/', views.AvatarView.as_view({"post": "update"})),
    path('upload/avatar/<str:username>/', views.AvatarView.as_view({"post": "update"})),
    path('login/', obtain_jwt_token),
    # path('login/', views.Login.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('info/', views.UserView.as_view({"get": "list"})),
    path('info/<str:username>', views.UserView.as_view({"post": "update"})),

    re_path(r'^(?P<username>\w{6,20})/count/$', views.UsernameValidateView.as_view(), name='check_username'),
    re_path(r'^(?P<email>[A-Za-z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9_-]+)/count/$', views.EmailValidateView.as_view(),
            name='check_email'),
]


