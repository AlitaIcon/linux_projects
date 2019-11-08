#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:09
# @Author  : icon
# @File    : serializer.py


from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from testcases.models import TestCases


class TestCasesModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label='用例名称', max_length=200, min_length=6, help_text='用例名称',
                                 validators=[UniqueValidator(queryset=TestCases.objects.all(),
                                                             message='用例名称不可重复')],
                                 error_messages={
                                     'max_length': '长度不超过200字节',
                                     'min_length': '长度不小于6字节',
                                 })

    class Meta:
        model = TestCases
        fields = "__all__"


class TestCasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCases
        fields = ("id", "name")
