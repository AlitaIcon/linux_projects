import json

# Create your views here.
import os
from datetime import datetime

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from envs.models import Envs
from interfaces.models import Interfaces
from learnDjango.settings import SUITES_DIR
from testcases.models import TestCases
from testcases.serializer import TestCasesModelSerializer, TestcasesRunSerializer
from utils import handle_datas, common


class TestCasesViewSet(ModelViewSet):
    """
    list:
    返回用例（多个）列表数据

    create:
    创建用例

    retrieve:
    返回用例（单个）详情数据

    update:
    更新（全）用例

    partial_update:
    更新（部分）用例

    destroy:
    删除用例

    run:
    运行用例

    details:
    获取用例详情
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

    def retrieve(self, request, *args, **kwargs):
        """获取用例详情信息"""
        # Testcase对象
        testcase_obj = self.get_object()

        # 用例前置信息
        testcase_include = json.loads(testcase_obj.include, encoding='utf-8')

        # 用例请求信息
        testcase_request = json.loads(testcase_obj.request, encoding='utf-8')
        testcase_request_datas = testcase_request.get('test').get('request')

        # 处理用例的validate列表
        # 将[{'check': 'status_code', 'expected':200, 'comparator': 'equals'}]
        # 转化为[{key: 'status_code', value: 200, comparator: 'equals', param_type: 'string'}]
        testcase_validate = testcase_request.get('test').get('validate')
        testcase_validate_list = handle_datas.handle_data1(testcase_validate)

        # 处理用例的param数据
        testcase_params = testcase_request_datas.get('params')
        testcase_params_list = handle_datas.handle_data4(testcase_params)

        # 处理用例的header列表
        testcase_headers = testcase_request_datas.get('headers')
        testcase_headers_list = handle_datas.handle_data4(testcase_headers)

        # 处理用例variables变量列表
        testcase_variables = testcase_request.get('test').get('variables')
        testcase_variables_list = handle_datas.handle_data2(testcase_variables)

        # 处理form表单数据
        testcase_form_datas = testcase_request_datas.get('data')
        testcase_form_datas_list = handle_datas.handle_data6(testcase_form_datas)

        # 处理json数据
        # testcase_json_datas = str(testcase_request_datas.get('json'))
        testcase_json_datas = json.dumps(testcase_request_datas.get('json'), ensure_ascii=False)

        # 处理extract数据
        testcase_extract_datas = testcase_request.get('test').get('extract')
        testcase_extract_datas_list = handle_datas.handle_data3(testcase_extract_datas)

        # 处理parameters数据
        testcase_parameters_datas = testcase_request.get('test').get('parameters')
        testcase_parameters_datas_list = handle_datas.handle_data3(testcase_parameters_datas)

        # 处理setupHooks数据
        testcase_setup_hooks_datas = testcase_request.get('test').get('setup_hooks')
        testcase_setup_hooks_datas_list = handle_datas.handle_data5(testcase_setup_hooks_datas)

        # 处理teardownHooks数据
        testcase_teardown_hooks_datas = testcase_request.get('test').get('teardown_hooks')
        testcase_teardown_hooks_datas_list = handle_datas.handle_data5(testcase_teardown_hooks_datas)

        selected_configure_id = testcase_include.get('config')
        selected_interface_id = testcase_obj.interface_id
        selected_project_id = Interfaces.objects.get(id=selected_interface_id).project_id
        selected_testcase_id = testcase_include.get('testcases')

        datas = {
            "author": testcase_obj.author,
            "testcase_name": testcase_obj.name,
            "selected_configure_id": selected_configure_id,
            "selected_interface_id": selected_interface_id,
            "selected_project_id": selected_project_id,
            "selected_testcase_id": selected_testcase_id,

            "method": testcase_request_datas.get('method'),
            "url": testcase_request_datas.get('url'),
            "param": testcase_params_list,
            "header": testcase_headers_list,
            "variable": testcase_form_datas_list,   # form表单请求数据
            "jsonVariable": testcase_json_datas,

            "extract": testcase_extract_datas_list,
            "validate": testcase_validate_list,
            "globalVar": testcase_variables_list,   # 变量
            "parameterized": testcase_parameters_datas_list,
            "setupHooks": testcase_setup_hooks_datas_list,
            "teardownHooks": testcase_teardown_hooks_datas_list,
        }
        return Response(datas)

    @action(methods=['post'], detail=True)
    def run(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        datas = serializer.validated_data
        env_id = datas.get("env_id")
        # testcase_dir_path = SUITES_DIR
        testcase_dir_path = os.path.join(SUITES_DIR, datetime.strftime(datetime.now(), '%Y%m%d%M%H%S%f'))
        if not os.path.exists(testcase_dir_path):
            os.mkdir(testcase_dir_path)

        env = Envs.objects.filter(id=env_id, is_delete=False).first()

        # 生成yaml用例文件
        common.generate_testcase_files(instance, env, testcase_dir_path)
        return common.run_testcase(instance, testcase_dir_path)

    def get_serializer_class(self):
        return TestcasesRunSerializer if self.action == "run" else TestCasesModelSerializer
