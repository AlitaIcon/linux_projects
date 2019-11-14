#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/6 21:06
# @Author  : icon
# @File    : utils.py
import re

from django.db.models import Count

from interfaces.models import Interfaces
from testsuites.models import TestSuites


def format_output(datas):
    data_list = []
    for item in datas:
        item['result'] = "Pass" if item['result'] else "Fail"
        if not item.get("is_delete"):
            data_list.append(item)

    return data_list


def get_file_contents(filename, chunk_size=512):
    with open(filename, encoding='utf-8') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break
