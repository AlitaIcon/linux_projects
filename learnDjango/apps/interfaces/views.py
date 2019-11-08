import json

from django.http import JsonResponse, Http404
# Create your views here.
from django.views import View
from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from configures.models import Configures
from interfaces.models import Interfaces
from interfaces.serializer import InterfaceModelSerializer, InterfaceNameSerializer


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
from interfaces.utils import get_count_by_project
from testcases.models import TestCases


class InterfaceViewSet(ModelViewSet):
    """
     create:
    创建接口

    retrieve:
    获取接口详情数据

    update:
    完整更新接口

    partial_update:
    部分更新接口

    destroy:
    删除接口

    list:
    获取接口列表数据

    names:
    获取所有接口名称
    """
    queryset = Interfaces.objects.all()
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

    @action(methods=['get'], detail=True, url_path='configs')
    def configures(self, request, pk=None):
        configures_models = Configures.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in configures_models:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

    @action(methods=['get'], detail=True, url_path='testcases')
    def testcases(self, request, pk=None):
        testcases_models = TestCases.objects.filter(interface_id=pk, is_delete=False)
        one_list = []
        for obj in testcases_models:
            one_list.append({
                'id': obj.id,
                'name': obj.name,
                'status_code': 200
            })
        return Response(data=one_list)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = get_count_by_project(serializer.data)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = get_count_by_project(serializer.data)
        return Response(data)

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()
