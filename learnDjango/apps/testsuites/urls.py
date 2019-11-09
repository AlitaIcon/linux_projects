#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 21:05
# @Author  : icon
# @File    : urls.py

from rest_framework.routers import DefaultRouter
from testsuites import views

router = DefaultRouter()

router.register(r'testsuites', views.TestSuitesViewSet, basename='testsuites')
urlpatterns = [
]
urlpatterns += router.urls
