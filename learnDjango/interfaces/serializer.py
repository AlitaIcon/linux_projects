#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py


from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from interfaces.models import Interface

# 单字段校验
from projects.models import Projects
from projects.serializer import ProjectModelSerializer


def is_unique_name(name):
    if '接口' not in name:
        raise serializers.ValidationError('接口名称必须包含“接口”')


class InterfaceSerializer(serializers.Serializer):
    # 需要输出那些字段，就在序列化器中定义哪些字段
    # read_only 只能序列化输出，不能反序列化输入
    # write_only 只能反序列化输入，不能序列化输出
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='接口名称', max_length=200, help_text='接口名称', write_only=True,
                                 validators=[UniqueValidator(queryset=Interface.objects.all(),
                                                             message='接口名称不可重复'), is_unique_name])
    url = serializers.CharField(label='接口地址', max_length=100, help_text='接口地址')
    data = serializers.CharField(label='参数', max_length=100, allow_blank=True, allow_null=True, help_text='接口参数')
    projects_id = serializers.IntegerField(label='所属接口', help_text='所属接口')

    def create(self, validated_data):
        return Interface.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.url = validated_data['url']
        instance.data = validated_data['data']
        instance.projects_id = validated_data['projects_id']
        instance.save()
        return instance

    # 单字段的校验
    def validate_name(self, value):
        if not value.endswith('接口'):
            raise serializers.ValidationError('接口必须以"接口"结尾')
        return value

    # 多字段校验
    def validate(self, attrs):
        if 'login' not in attrs['name'] and 'login' not in attrs['url']:
            raise serializers.ValidationError('接口名称或URL必须包含login')
        return attrs


class InterfaceModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='接口名称', max_length=200, min_length=6, help_text='接口名称', write_only=True,
                                 # validators中的验证器会全部执行，如果抛异常，则不执行单字段验证器和联合字段验证器
                                 validators=[UniqueValidator(queryset=Interface.objects.all(),
                                                             message='接口名称不可重复'), is_unique_name],
                                 error_messages={
                                     'max_length': '长度不超过200字节',
                                     'min_length': '长度不小于6字节',
                                 })
    # 1.数据库模型中的外键字段，默认会生成PrimaryKeyRelatedField序列化器字段
    # projects = serializers.PrimaryKeyRelatedField(read_only=True)
    # 2.StringRelatedField，此字段将被序列化器为关联对象字符串表达形式（即__str__()返回值）
    # projects = serializers.StringRelatedField(label='所属项目')
    # 3.SlugRelatedField，此字段将被序列化器为关联对象的字段数据
    # projects = serializers.SlugRelatedField(label='所属项目', slug_field="leader", read_only=True)
    # projects = serializers.SlugRelatedField(label='所属项目', slug_field="leader", queryset=Interface.objects.all())
    # 4.使用关联对象的序列化器
    projects = ProjectModelSerializer(label='所属项目')

    class Meta:
        model = Interface
        fields = "__all__"
        # fields = ["id", "name", "url", "projects", "age"]  # 模型类未定义字段一定要在fields中定义
        # fields = ["id", "name", "url", "projects"]
        # exclude = ("data", "projects")
        # read_only_fields = ('id', 'name')
        # ordering_fields = ['name']
        extra_kwargs = {
            'url': {'write_only': True, 'error_messages': {'max_length': '长度不超过200字节', 'min_length': '长度不小于20字节'}}
        }

    # 单字段的校验
    def validate_name(self, value):
        if not value.endswith('接口'):
            raise serializers.ValidationError('接口必须以"接口"结尾')
        return value

    # 多字段校验
    def validate(self, attrs):
        if 'login' not in attrs['name'] and 'login' not in attrs['url']:
            raise serializers.ValidationError('接口名称或URL必须包含login')
        return attrs


class InterfaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = ['id', 'name']


from projects.serializer import ProjectsNameSerializer


class ProjectsByInterfaceSerializer(serializers.ModelSerializer):
    # 重写序列化器中的模型类字段
    url = serializers.CharField(max_length=200, default='')
    projects = ProjectsNameSerializer()
    interface_url = url  # 更改序列化器的模型类中的字段名

    class Meta:
        model = Interface
        fields = ['url', 'interface_url', 'projects']
