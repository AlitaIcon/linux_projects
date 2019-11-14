# Create your views here.
import json

from rest_framework.decorators import action

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from configures.models import Configures
from configures.serializer import ConfigureModelSerializer, ConfiguresNameSerializer
from configures.utils import get_count_by_project
from interfaces.models import Interfaces
from utils import handle_datas


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
        return res

    def retrieve(self, request, *args, **kwargs):
        config_obj = self.get_object()
        config_request = json.loads(config_obj.request, encoding='utf-8')

        # 处理请求头数据
        # config_headers = config_request['config']['request']['headers']
        config_headers = config_request['config']['request'].get('headers')
        config_headers_list = handle_datas.handle_data4(config_headers)

        # 处理全局变量数据
        # config_variables = config_request['config']['variables']
        config_variables = config_request['config'].get('variables')
        config_variables_list = handle_datas.handle_data2(config_variables)

        config_name = config_request['config']['name']
        selected_interface_id = config_obj.interface_id
        selected_project_id = Interfaces.objects.get(id=selected_interface_id).project_id

        datas = {
            "author": config_obj.author,
            "configure_name": config_name,
            "selected_interface_id": selected_interface_id,
            "selected_project_id": selected_project_id,
            "header": config_headers_list,
            "globalVar": config_variables_list
        }

        return Response(datas)
