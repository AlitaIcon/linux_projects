#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/4 8:58
# @Author  : icon
# @File    : MyPermission.py


from rest_framework import permissions


class MyPermission(permissions.BasePermission):
    message = 'admin用户才有该权限'

    def has_permission(self, request, view):
        """
        自定义权限只有admin用户才能访问
        """
        # 因为在进行权限判断之前已经做了认证判断，所以这里可以直接拿到request.user
        if request.method in permissions.SAFE_METHODS:  # 如果是admin用户
            return True
        token = request.headers.get("Authorization", 0)
        if token:
                return request.user.is_staff
        return False
