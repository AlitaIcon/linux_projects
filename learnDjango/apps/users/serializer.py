#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/10/29 10:44
# @Author  : icon
# @File    : serializer.py
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.validators import MinLengthValidator
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(label='确认密码', help_text='确认密码',
                                             min_length=6, max_length=20,
                                             write_only=True, error_messages={
            'min_length': '仅允许6-20位字符',
            'max_length': '仅允许6-20位字符'})

    token = serializers.CharField(label='生成token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'password_confirm', 'token', 'phone')
        # unique_together = ('email',)
        extra_kwargs = {
            'phone': {
                'label': '手机号',
                'help_text': '手机号',
                'min_length': 11,
                'max_length': 11,
                # 'validators': [UniqueValidator(queryset=User.objects.all(), message="该手机号已被注册")],
                'error_messages': {
                    'min_length': '手机号仅能为11位',
                    'max_length': '手机号仅能为11位',
                }
            },
            'username': {
                'label': '用户名',
                'help_text': '用户名',
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的用户名',
                    'max_length': '仅允许6-20个字符的用户名',
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                # 'unique': True,  # 因为allow_blank=True，且序列化器中没有该字段
                'validators': [UniqueValidator(queryset=User.objects.all(), message="该邮箱已被注册")]
            },
            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许6-20个字符的密码',
                    'max_length': '仅允许6-20个字符的密码',
                }
            }
        }

    def create(self, validated_data):
        validated_data.pop("password_confirm")
        # validated_data['password'] = make_password(validated_data['password'])
        # user = User.objects.create(**validated_data)
        user = User.objects.create_user(**validated_data)  # 使用User内置的create_user
        # user.set_password(user.password)
        # user.save()
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token
        return user

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")
        if password != password_confirm:
            raise serializers.ValidationError('密码要和确认密码一致')
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = ("is_admin",)
        read_only_fields = ("username",)
        # ordering_fields = ("id", )
        extra_kwargs = {
            'password': {
                'label': '密码',
                'help_text': '密码',
                'write_only': True,
                'min_length': 6,
                # 'max_length': 255,  # 为了加密保存
                'error_messages': {
                    'min_length': '密码最小为6位',
                    # 'max_length': '密码最大为255位',
                }
            },
            'phone': {
                'label': '手机号',
                'help_text': '手机号',
                'min_length': 11,
                'max_length': 11,
                # 'validators': [UniqueValidator(queryset=User.objects.all(), message="该手机号已被注册"),
                               # MinLengthValidator(11, message="手机号仅能为11位")
                               # ],
                'error_messages': {
                    'min_length': '手机号仅能为11位',
                    'max_length': '手机号仅能为11位',
                }
            },
            'email': {
                'label': '邮箱',
                'help_text': '邮箱',
                'write_only': True,
                'required': True,
                # 'unique': True,  # 因为allow_blank=True，且序列化器中没有该字段
                'validators': [UniqueValidator(queryset=User.objects.all(), message="该邮箱已被注册")]
            },
        }


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('created_time', 'last_login')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        date_joined = ret.pop('created_time')
        ret['date_joined'] = date_joined
        return ret
