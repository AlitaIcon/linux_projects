#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py


from rest_framework import serializers
from debugtalks.models import DebugTalks


class DebugTalksModelSerializer(serializers.ModelSerializer):
    project = serializers.StringRelatedField(help_text="项目名称")

    class Meta:
        model = DebugTalks
        # fields = "__all__"
        exclude = ("is_delete", "update_time")
        read_only_fields = ("create_time",)
        # write_only_fields = ("debugtalk",) 不能这么写
        extra_kwargs = {
            'debugtalk': {'write_only': True}
        }


class DebugTalksNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DebugTalks
        fields = ("id", "name")
