import json

from django.http import JsonResponse, Http404
# Create your views here.
from django.views import View
from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.generics import GenericAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import mixins
from interfaces.models import Interface
from interfaces.serializer import InterfaceModelSerializer, InterfaceNameSerializer, ProjectsByInterfaceSerializer
from utils.pagination import PageNumberPaginationManual


# ViewSet未提供get_object() get_serializer() queryset serializer_class
# 所以要继承GenericViewSet
# class InterfaceViewSet(mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         mixins.UpdateModelMixin,
#                         mixins.DestroyModelMixin,
#                         mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     queryset = Interface.objects.all()  # 指定查询集
#     serializer_class = InterfaceModelSerializer
#     # ordering_fields = ['name']  # 可指定多字段排序
#     filterset_fields = ['id', 'name']  # 指定需要过滤的字段


class InterfaceViewSet(ModelViewSet):
    """
     create:
    创建项目

    retrieve:
    获取项目详情数据

    update:
    完整更新项目

    partial_update:
    部分更新项目

    destroy:
    删除项目

    list:
    获取项目列表数据

    names:
    获取所有接口名称

    projects:
    获取接口下项目
    """
    queryset = Interface.objects.all()
    serializer_class = InterfaceModelSerializer
    ordering_fields = ['name']
    filterset_fields = ['id', 'name']

    # 使用action装饰器来声明自定义动作
    # 默认情况下，实例方法是动作名
    # method默认为get，指定方法的请求方法
    # detail参数指定该动作处理的是否为详情资源对象（url是否需要传递pk键值）
    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = InterfaceNameSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True)
    def projects(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProjectsByInterfaceSerializer(instance=instance)
        return Response(serializer.data)
