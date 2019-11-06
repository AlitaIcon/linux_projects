#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/10/12 13:03
# @Author  : icon
# @File    : urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from interfaces import views

router = DefaultRouter()
# router = SimpleRouter()
router.register(r'interfaces', views.InterfaceViewSet, basename='interfaces')
urlpatterns = [
    # path(r'', include(router.urls)),
    # path('', views.InterfaceViewSet.as_view({
    #     'get': 'list',
    #     'post': 'create'
    # }), name='interfaces-list'),
    # path('<int:pk>/', views.InterfaceViewSet.as_view({
    #     'get': 'retrieve',
    #     'put': 'update',
    #     'delete': 'destroy'
    # })),
    # 使用router注册路由后，就不用手动指定路由了
    # path('interfaces/names/', views.InterfaceViewSet.as_view({
    #     'get': 'names'
    # }), name='interface-names'),
    # path('<int:pk>/projects/', views.InterfaceViewSet.as_view({
    #     'get': 'projects'
    # }), name='interface-projects'),

]
urlpatterns += router.urls
# urlpatterns = router.urls