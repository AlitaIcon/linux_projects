#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 21:12
# @Author  : icon
# @File    : serializer.py

from rest_framework import serializers

from projects.models import Projects
from testsuites.models import TestSuites
from utils import validates


class TestSuitesModelSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(label="Project ID", queryset=Projects.objects.all())
    project = serializers.StringRelatedField(label='所属项目')

    class Meta:
        model = TestSuites
        exclude = ("is_delete",)
        read_only_fields = ('create_time',)
        ordering = ("id", "name")

    def create(self, validated_data):
        project = validated_data.pop("project_id")
        validated_data["project"] = project
        return TestSuites.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'project_id' in validated_data:
            project = validated_data.pop("project_id")
            validated_data["project"] = project
        return super().update(instance, validated_data)


class TestSuitesNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuites
        fields = ("id", "name")


class TestsSuitesRunSerializer(serializers.ModelSerializer):
    """
    通过套件来运行测试用例序列化器
    """
    env_id = serializers.IntegerField(write_only=True,
                                      help_text='环境变量ID',
                                      validators=[validates.whether_existed_env_id])

    class Meta:
        model = TestSuites
        fields = ('id', 'env_id')
