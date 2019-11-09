# Create your views here.

from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from envs.models import Envs
from envs.serializer import EnvsModelSerializer, EnvNameSerializer


class EnvsViewSet(ModelViewSet):
    """
     create:
    创建环境变量

    retrieve:
    获取环境变量详情数据

    update:
    完整更新环境变量

    partial_update:
    部分更新环境变量

    destroy:
    删除环境变量

    list:
    获取环境变量列表数据

    names:
    获取所有环境变量名称
    """
    queryset = Envs.objects.all()
    serializer_class = EnvsModelSerializer
    ordering_fields = ['name']
    filterset_fields = ['id', 'name']

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "names":
            return EnvNameSerializer
        return self.serializer_class
