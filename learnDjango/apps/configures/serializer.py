#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py

from rest_framework import serializers
from configures.models import Configures

from interfaces.models import Interfaces
from utils.validates import whether_existed_project_id, whether_existed_interface_id


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


class ConfigureModelSerializer(serializers.ModelSerializer):
    interface = InterfacesAnotherSerializer(help_text="接口名称")

    class Meta:
        model = Configures
        exclude = ("is_delete", "update_time")
        # fields = "__all__"
        # read_only_fields = ("create_time",)
        extra_kwargs = {
            'request': {"write_only": True},
        }

    def create(self, validated_data):
        interface_dict = validated_data.pop('interface')
        validated_data['interface_id'] = interface_dict['iid']
        return Configures.objects.create(**validated_data)

    def update(self, instance, validated_data):
        if 'interface' in validated_data:
            interface_dict = validated_data.pop('interface')
            validated_data['interface_id'] = interface_dict['iid']
        return super().update(**validated_data)


class ConfiguresNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configures
        fields = ("id", "name")


