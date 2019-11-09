from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from interfaces.models import Interfaces
from testcases.models import TestCases
from testcases.serializer import TestCasesModelSerializer, TestCasesSerializer


class TestCasesViewSet(ModelViewSet):
    """
     create:
    创建用例

    retrieve:
    获取用例详情数据

    update:
    完整更新用例

    partial_update:
    部分更新用例

    destroy:
    删除用例

    list:
    获取用例列表数据

    names:
    获取所有用例名称
    """
    queryset = TestCases.objects.all()
    serializer_class = TestCasesModelSerializer
    ordering_fields = ['name']
    filterset_fields = ['id', 'name']

    def create(self, request, *args, **kwargs):
        data = request.data
        interface = data.get("interface").get("iid")
        data["interface"] = interface
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['get'], detail=True)
    def details(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance)
        data = serializer.data
        interface_id = serializer.data.get("interface")
        selected_project_id = Interfaces.objects.get(id=interface_id, is_delete=False).project_id
        data['selected_project_id'] = selected_project_id
        data['selected_interface_id'] = interface_id
        data['selected_testcase_id'] = int(kwargs.get("pk"))
        data['selected_configure_id'] = Interfaces.objects.get(id=interface_id).configures.instance.id
        return Response(data)
