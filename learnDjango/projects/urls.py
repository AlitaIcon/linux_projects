#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 21:05
# @Author  : icon
# @File    : urls.py


from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from projects import views
# 1.创建SimpleRouter路由对象
router = SimpleRouter(trailing_slash=False)  # trailing_slash=False，会将路由最后面斜杠去除
# router = DefaultRouter()
# 2.注册路由，第一个参数prefix，一般为应用名即可，第二个viewset为视图集，不加as_view()
router.register(r'projects', views.ProjectsViewSet, basename='projects')
urlpatterns = [
    # path('projects/', views.ProjectsViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }), name='projects-list'),
    # path('projects/<int:pk>/', views.ProjectsViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    # path('projects/<int:pk>/interfaces/', views.ProjectsViewSet.as_view({
    #     'get': 'interfaces'
    # }), name='projects-interfaces')
]
urlpatterns += router.urls
