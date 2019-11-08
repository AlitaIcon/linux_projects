#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/6 21:06
# @Author  : icon
# @File    : utils.py
import re

from django.db.models import Count

from testcases.models import TestCases
from configures.models import Configures


def get_count_by_project(datas):
    data_list = []
    for item in datas:
        # match = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        # item['create_time'] = match.group(1) + " " + match.group(2)
        interface_id = item["id"]
        testcases_count = TestCases.objects.filter(interface_id=interface_id, is_delete=False).count()
        configures_count = Configures.objects.filter(interface_id=interface_id, is_delete=False).count()
        item["testcases_count"] = testcases_count
        item["configures_count"] = configures_count
        data_list.append(item)

    return data_list
