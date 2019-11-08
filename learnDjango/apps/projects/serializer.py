#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 21:12
# @Author  : icon
# @File    : serializer.py
import datetime

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from projects.models import Projects


class ProjectModelSerializer(serializers.ModelSerializer):
    # interfaces = InterfaceInfoSerializer(many=True)
    # interfaces = serializers.StringRelatedField(many=True, read_only=True)
    # interfaces = InterfaceInfoSerializer(many=True, read_only=True)
    # testsuites = serializers.StringRelatedField(many=True, read_only=True)
    # created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Projects
        exclude = ("is_delete", "update_time")
        read_only_fields = ('created_time',)
        ordering = ("id", "name")
        extra_kwargs = {
            'name': {'label': '项目名称', 'max_length': 50, 'help_text': '项目名称', 'validators': [
                UniqueValidator(queryset=Projects.objects.all(), message='项目名称不可重复')],
                     'error_messages': {'max_length': '长度不超过50字节'}},
            'leader': {'label': '项目负责人', 'max_length': 50, 'help_text': '项目负责人', 'error_messages': {
                'max_length': '长度不超过50字节'}},
            'tester': {'label': '测试人员', 'max_length': 50, 'help_text': '测试人员', 'error_messages': {
                'max_length': '长度不超过50字节'}},
            'programmer': {'label': '开发人员', 'max_length': 50, 'help_text': '开发人员', 'error_messages': {
                'max_length': '长度不超过50字节'}},
            'publish_app': {'label': '发布应用', 'max_length': 100, 'help_text': '发布应用', 'error_messages': {
                'max_length': '长度不超过100字节'}},
            'desc': {'label': '简要描述', 'max_length': 200, 'help_text': '简要描述', 'error_messages': {
                'max_length': '长度不超过200字节'}},
        }
    #
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['interfaces_len'] = len(ret['interfaces'])
    #     ret['testsuites_len'] = len(ret['testsuites'])
    #     if ret['interfaces']:
    #         ret['configures_len'] = sum([len(r['configures']) for r in ret['interfaces']])
    #         ret['testcases_len'] = sum([len(r['testcases']) for r in ret['interfaces']])
    #         return ret
    #     ret['configures_len'] = 0
    #     ret['testcases_len'] = 0
    #     return ret


class ProjectNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "name")
