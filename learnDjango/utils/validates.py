#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/12 9:27
# @Author  : icon
# @File    : validates.py
from rest_framework import serializers

from envs.models import Envs
from interfaces.models import Interfaces
from projects.models import Projects


def whether_existed_interface_id(value):
    if not isinstance(value, int):
        raise serializers.ValidationError('所选项目有误!')
    if not Interfaces.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError('所选项目不存在!')
    return True


def whether_existed_project_id(value):
    if not isinstance(value, int):
        raise serializers.ValidationError('所选项目有误!')
    if not Projects.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError('所选项目不存在!')
    return True


def whether_existed_env_id(value):
    if not isinstance(value, int):
        raise serializers.ValidationError('所选环境有误!')
    if not Envs.objects.filter(is_delete=False, id=value).exists():
        raise serializers.ValidationError('所选环境不存在!')
    return True
