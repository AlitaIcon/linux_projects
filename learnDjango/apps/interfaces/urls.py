#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/10/12 13:03
# @Author  : icon
# @File    : urls.py
from rest_framework.routers import DefaultRouter
from interfaces import views

router = DefaultRouter()
router.register(r'interfaces', views.InterfaceViewSet, basename='interfaces')
urlpatterns = [
    # path(r'', include(router.urls)),
]
urlpatterns += router.urls
