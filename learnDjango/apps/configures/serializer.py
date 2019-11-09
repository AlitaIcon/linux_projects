#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py

from rest_framework import serializers
from configures.models import Configures


class ConfigureModelSerializer(serializers.ModelSerializer):
    interface = serializers.StringRelatedField(help_text="接口名称")

    class Meta:
        model = Configures
        exclude = ("is_delete", "update_time")
        # fields = "__all__"
        read_only_fields = ("create_time",)

    # def create(self, validated_data):
    #     pass


class ConfiguresNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configures
        fields = ("id", "name")

