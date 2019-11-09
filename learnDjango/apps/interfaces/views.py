# Create your views here.

from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from configures.models import Configures
from interfaces.models import Interfaces
from interfaces.serializer import InterfaceModelSerializer, InterfaceNameSerializer

from interfaces.utils import get_count_by_project
from projects.serializer import ProjectNameSerializer
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

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
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
        res = super().list(request, *args, **kwargs)
        res.data["results"] = get_count_by_project(res.data.get("results"))
        return res

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def get_serializer_class(self):
        if self.action == "names":
            return ProjectNameSerializer
        return self.serializer_class
