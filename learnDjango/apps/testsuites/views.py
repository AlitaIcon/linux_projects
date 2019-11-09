# Create your views here.

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from testsuites.models import TestSuites
from testsuites.utils import get_count_by_project
from testsuites.serializer import TestSuitesModelSerializer, TestSuitesNameSerializer


class TestSuitesViewSet(ModelViewSet):
    """
     create:
    创建测试套件

    retrieve:
    获取测试套件详情数据

    update:
    完整更新测试套件

    partial_update:
    部分更新测试套件

    destroy:
    删除测试套件

    list:
    获取测试套件列表数据

    names:
    获取所有测试套件名称
    """
    queryset = TestSuites.objects.all()
    serializer_class = TestSuitesModelSerializer
    ordering_fields = ['name']
    filterset_fields = ['id', 'name']

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        res.data["results"] = get_count_by_project(res.data.get("results"))
        return res

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def get_serializer_class(self):
        if self.action == "names":
            return TestSuitesNameSerializer
        return self.serializer_class
