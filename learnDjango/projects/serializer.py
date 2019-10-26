#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 21:12
# @Author  : icon
# @File    : serializer.py
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Projects


def is_unique_name(name):
    if '项目' not in name:
        raise serializers.ValidationError('接口名称必须包含“项目”')


class ProjectModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='项目名称', max_length=200, min_length=6, help_text='项目名称', write_only=True,
                                 validators=[UniqueValidator(queryset=Projects.objects.all(),
                                                             message='项目名称不可重复'), is_unique_name],
                                 error_messages={
                                     'max_length': '长度不超过200字节',
                                     'min_length': '长度不小于6字节',
                                 })

    interface_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = Projects
        fields = "__all__"
        # fields = ["des", "name", "leader"]
        # exclude = ("data", "projects")
        # read_only_fields = ('id', 'name')
        extra_kwargs = {
            'des': {'write_only': True, 'error_messages': {'max_length': '长度不超过200字节', 'min_length': '长度不小于20字节'}}
        }

    # 单字段的校验
    def validate_name(self, value):
        if not value.endswith('项目'):
            raise serializers.ValidationError('项目必须以"项目"结尾')
        return value

    # 多字段校验
    def validate(self, attrs):
        if '项目' not in attrs['name'] and '项目' not in attrs['des']:
            raise serializers.ValidationError('项目名称或描述必须包含“项目”')
        return attrs

    def __str__(self):
        return self.name


class ProjectsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'name']


# 防止互相引入导致报错
from interfaces.serializer import InterfaceNameSerializer


class InterfaceByProjectsIdSerializer(serializers.ModelSerializer):
    interface_set = InterfaceNameSerializer(read_only=True, many=True)

    class Meta:
        model = Projects
        fields = ['name', 'interface_set']


