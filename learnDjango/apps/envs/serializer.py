#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py


from rest_framework import serializers
from envs.models import Envs


class EnvsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = "__all__"
        # exclude = ("is_delete", "update_time")
        read_only_fields = ("create_time",)


class EnvNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envs
        fields = ("id", "name")
