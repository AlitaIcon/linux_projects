# Create your views here.
from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from configures.models import Configures
from configures.serializer import ConfigureModelSerializer, ConfiguresNameSerializer
from configures.utils import get_count_by_project


class ConfiguresViewSet(ModelViewSet):
    """
     create:
    创建配置

    retrieve:
    获取配置详情数据

    update:
    完整更新配置

    partial_update:
    部分更新配置

    destroy:
    删除配置

    list:
    获取配置列表数据

    names:
    获取所有配置名称
    """
    queryset = Configures.objects.all()
    serializer_class = ConfigureModelSerializer
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
            return ConfiguresNameSerializer
        return self.serializer_class

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        res.data["results"] = get_count_by_project(res.data.get("results"))
        return res
