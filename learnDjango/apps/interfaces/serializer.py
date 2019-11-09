#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py


from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from interfaces.models import Interfaces
from projects.models import Projects


class InterfaceModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='接口名称', max_length=200, min_length=6, help_text='接口名称',
                                 # validators中的验证器会全部执行，如果抛异常，则不执行单字段验证器和联合字段验证器
                                 validators=[UniqueValidator(queryset=Interfaces.objects.all(),
                                                             message='接口名称不可重复')],
                                 error_messages={
                                     'max_length': '长度不超过200字节',
                                     'min_length': '长度不小于6字节',
                                 })
    project_id = serializers.PrimaryKeyRelatedField(label="Project ID", queryset=Projects.objects.all())
    project = serializers.StringRelatedField(label='所属项目')

    class Meta:
        model = Interfaces
        # fields = "__all__"
        fields = ("id", "project", "project_id", "name", "tester", "desc", "create_time")
        # exclude = ("is_delete", "update_time")
        read_only_fields = ("create_time",)

    def create(self, validated_data):
        project = validated_data.pop("project_id")
        validated_data["project"] = project
        return Interfaces.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop("project_id")
            validated_data["project"] = project
        return super().update(instance, validated_data)


class InterfaceInfoSerializer(serializers.ModelSerializer):
    configures = serializers.StringRelatedField(many=True, read_only=True)
    testcases = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Interfaces
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['configures_len'] = len(ret['configures'])
        ret['testcases_len'] = len(ret['testcases'])
        return ret


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interfaces
        fields = ("id", "name")


# from projects.serializer import ProjectsNameSerializer
#
#
# class ProjectsByInterfaceSerializer(serializers.ModelSerializer):
#     # 重写序列化器中的模型类字段
#     url = serializers.CharField(max_length=200, default='')
#     projects = ProjectsNameSerializer()
#     interface_url = url  # 更改序列化器的模型类中的字段名
#
#     class Meta:
#         model = Interfaces
#         fields = ['url', 'interface_url', 'projects']
