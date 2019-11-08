#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/4 14:59
# @Author  : icon
# @File    : model_tools.py
import datetime
import os

from django.db import models

ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# TODO:同名文件要处理
def upload_to(instance, filename):
    image_dir = "image/avatar/"
    ext = filename.split('.').pop()
    if allowed_file(filename):
        filename = '{0}{1}.{2}'.format(instance.username[:2], instance.phone[-4:], ext)
        return os.path.join(image_dir, filename)  # 系统路径分隔符差异，增强代码重用性
    return "image/avatar/default.png"


class BaseModel(models.Model):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    create_time = models.DateTimeField(auto_now_add=datetime.datetime.now, verbose_name="创建时间", help_text="创建时间")
    update_time = models.DateTimeField(auto_now=datetime.datetime.now, verbose_name="更新时间", help_text="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除", help_text="逻辑删除")

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        verbose_name_plural = verbose_name
