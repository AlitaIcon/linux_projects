#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 21:05
# @Author  : icon
# @File    : urls.py

from rest_framework.routers import DefaultRouter
from reports import views

router = DefaultRouter()

router.register(r'reports', views.ReportsViewSet, basename='reports')
urlpatterns = [
]
urlpatterns += router.urls
