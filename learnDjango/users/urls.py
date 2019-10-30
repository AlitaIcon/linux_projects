#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/10/29 8:57
# @Author  : icon
# @File    : urls.py


from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('register/', views.RegisterView.as_view())
]


