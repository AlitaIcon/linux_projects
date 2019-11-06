#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/4 10:13
# @Author  : icon
# @File    : MyAuth.py


from rest_framework.authentication import BaseAuthentication, TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class MyAuth(TokenAuthentication):
    """
    重写token认证，判断请求头是否有token认证
    """
    def authenticate(self, request):
        if request.method in ["POST", "PUT", "DELETE"]:
            request_token = request.headers.get("Authorization")
            if not request_token:
                raise AuthenticationFailed('尚未认证')



