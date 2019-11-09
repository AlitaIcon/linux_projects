#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/18 21:12
# @Author  : icon
# @File    : serializer.py
from _datetime import datetime

from rest_framework import serializers
from reports.models import Reports


class ReportsModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reports
        exclude = ("update_time", )
        read_only_fields = ('create_time',)
        ordering = ("id", "name")
        extra_kwargs = {
            'html': {'write_only': True},
            'is_delete': {'write_only': True},
        }

    def create(self, validated_data):
        report_name = validated_data['name']
        validated_data['name'] = report_name + '_' + datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
        return Reports.objects.create(**validated_data)


class ReportsNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ("id", "name")
