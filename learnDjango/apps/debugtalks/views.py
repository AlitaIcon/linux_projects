# Create your views here.

from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from debugtalks.models import DebugTalks
from debugtalks.serializer import DebugTalksModelSerializer, DebugTalksNameSerializer


class DebugtalksViewSet(ModelViewSet):
    """
     create:
    创建debugtalk文件

    retrieve:
    获取debugtalk文件详情数据

    update:
    完整更新debugtalk文件

    partial_update:
    部分更新debugtalk文件

    destroy:
    删除debugtalk文件

    list:
    获取debugtalk文件列表数据

    names:
    获取所有debugtalk文件名称
    """
    queryset = DebugTalks.objects.all()
    serializer_class = DebugTalksModelSerializer
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
            return DebugTalksNameSerializer
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {
            "id": instance.id,
            "debugtalk": instance.debugtalk
        }
        return Response(data=data)
