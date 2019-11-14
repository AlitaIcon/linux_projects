# Create your views here.
import os
from datetime import datetime

from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet

from envs.models import Envs
from interfaces.models import Interfaces
from interfaces.serializer import InterfaceInfoSerializer
from learnDjango import settings
from projects.models import Projects
from projects.serializer import ProjectModelSerializer, ProjectNameSerializer, ProjectsRunSerializer
from projects.utils import get_count_by_project
from testcases.models import TestCases
from utils import common


class ProjectsViewSet(ModelViewSet):
    """
     list:
     返回项目（多个）列表数据

     create:
     创建项目

     retrieve:
     返回项目（单个）详情数据

     update:
     更新（全）项目

     partial_update:
     更新（部分）项目

     destroy:
     删除项目

     names:
     返回所有项目ID和名称

     interfaces:
     返回某个项目的所有接口信息（ID和名称）
     """
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    ordering_fields = ('id', 'name')
    filterset_fields = ['id', 'name']
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['get'], detail=True, url_path='interfaces')
    def interfaces(self, request, pk=None):
        interface_models = Interfaces.objects.filter(project_id=pk, is_delete=False)
        one_list = []
        for obj in interface_models:
            one_list.append({
                'id': obj.id,
                'name': obj.name
            })
        return Response(data=one_list)

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    @action(methods=['get'], detail=False)
    def names(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(instance=queryset, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        res.data["results"] = get_count_by_project(res.data.get("results"))
        return res

    @action(methods=['post'], detail=True)
    def run(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        datas = serializer.validated_data
        env_id = datas.get('env_id')  # 获取环境变量env_id

        # 创建测试用例所在目录名
        testcase_dir_path = os.path.join(settings.SUITES_DIR,
                                         datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f"))
        if not os.path.exists(testcase_dir_path):
            os.mkdir(testcase_dir_path)

        env = Envs.objects.filter(id=env_id, is_delete=False).first()
        interface_objs = Interfaces.objects.filter(is_delete=False, project=instance)

        if not interface_objs.exists():  # 如果此项目下没有接口, 则无法运行
            data_dict = {
                "detail": "此项目下无接口, 无法运行!"
            }
            return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)

        for inter_obj in interface_objs:
            testcase_objs = TestCases.objects.filter(is_delete=False, interface=inter_obj)

            for one_obj in testcase_objs:
                common.generate_testcase_files(one_obj, env, testcase_dir_path)

        # 运行用例
        return common.run_testcase(instance, testcase_dir_path)

    def get_serializer_class(self):
        """
        不同的action选择不同的序列化器
        :return:
        """
        if self.action == 'names':
            return ProjectNameSerializer
        elif self.action == 'run':
            return ProjectsRunSerializer
        else:
            return self.serializer_class
