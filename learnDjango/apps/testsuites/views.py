# Create your views here.
import os
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from envs.models import Envs
from learnDjango import settings
from testcases.models import TestCases
from testsuites.models import TestSuites
from testsuites.utils import get_count_by_project, get_testcases_by_interface_ids
from testsuites.serializer import TestSuitesModelSerializer, TestSuitesNameSerializer, TestsSuitesRunSerializer
from utils import common


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

    def retrieve(self, request, *args, **kwargs):
        """获取用例详情信息"""
        # Testcase对象
        testsuit_obj = self.get_object()

        datas = {
            "name": testsuit_obj.name,
            "project_id": testsuit_obj.project_id,
            "include": testsuit_obj.include
        }
        return Response(datas)

    def get_serializer_class(self):
        if self.action == "names":
            return TestSuitesNameSerializer
        elif self.action == "run":
            return TestsSuitesRunSerializer
        return self.serializer_class

    @action(methods=['post'], detail=True)
    def run(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        datas = serializer.validated_data
        env_id = datas.get('env_id')  # 获取环境变量env_id

        # 创建测试用例所在目录名
        # testcase_dir_path = settings.SUITES_DIR
        testcase_dir_path = os.path.join(settings.SUITES_DIR,
                                         datetime.strftime(datetime.now(), "%Y%m%d%H%M%S%f"))
        if not os.path.exists(testcase_dir_path):
            os.mkdir(testcase_dir_path)
        env = Envs.objects.filter(id=env_id, is_delete=False).first()
        include = eval(instance.include)
        if len(include) == 0:
            data_dict = {
                "detail": "此套件下未添加用例, 无法运行!"
            }
            return Response(data_dict, status=status.HTTP_400_BAD_REQUEST)

        # 将include中的接口id转化为此接口下的用例id
        include = get_testcases_by_interface_ids(include)
        for testcase_id in include:
            testcase_obj = TestCases.objects.filter(is_delete=False, id=testcase_id).first()
            if testcase_obj:
                common.generate_testcase_files(testcase_obj, env, testcase_dir_path)

        return common.run_testcase(instance, testcase_dir_path)

