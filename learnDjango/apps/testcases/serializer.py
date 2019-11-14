#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py


from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from interfaces.models import Interfaces
from testcases.models import TestCases
from utils.validates import whether_existed_project_id, whether_existed_interface_id, whether_existed_env_id


class InterfacesAnotherSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text='项目名称')
    pid = serializers.IntegerField(write_only=True, validators=[whether_existed_project_id], help_text='项目ID')
    iid = serializers.IntegerField(write_only=True, validators=[whether_existed_interface_id], help_text='接口ID')

    class Meta:
        model = Interfaces
        fields = ('iid', 'pid', 'project', 'name')
        extra_kwargs = {
            'name': {"read_only": True},
        }

    def validate(self, attrs):
        """
        校验项目ID是否与接口ID一致
        :param attrs:
        :return:
        """
        if not Interfaces.objects.filter(id=attrs['iid'], project_id=attrs['pid'], is_delete=False).exists():
            raise serializers.ValidationError("项目和接口信息不对应!")
        return attrs


class TestCasesModelSerializer(serializers.ModelSerializer):
    interface = InterfacesAnotherSerializer(help_text="所属接口和项目信息")

    class Meta:
        model = TestCases
        fields = ('id', 'name', 'interface', 'include', 'author', 'request')
        extra_kwargs = {
            'include': {
                'write_only': True
            },
            'request': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        interface_dict = validated_data.pop('interface')
        validated_data['interface_id'] = interface_dict['iid']
        return TestCases.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['iid']
        return super().update(instance, validated_data)


class TestcasesRunSerializer(serializers.ModelSerializer):
    """
    运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      validators=[whether_existed_env_id])

    class Meta:
        model = TestCases
        fields = ('id', 'env_id')

