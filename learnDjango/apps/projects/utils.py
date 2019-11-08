#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/6 21:06
# @Author  : icon
# @File    : utils.py
import re

from django.db.models import Count

from interfaces.models import Interfaces
from testsuites.models import TestSuites


def get_count_by_project(datas):
    data_list = []
    for item in datas:
        # match = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        # item['create_time'] = match.group(1) + " " + match.group(2)
        project_id = item["id"]
        interfaces_count = Interfaces.objects.filter(project_id=project_id, is_delete=False).count()
        testsuites_count = TestSuites.objects.filter(project_id=project_id, is_delete=False).count()
        testcases_count = Interfaces.objects.values('id').annotate(testcases_count=Count('testcases')).filter(project_id=project_id, is_delete=False)
        configures_count = Interfaces.objects.values('id').annotate(configures_count=Count('configures')).filter(project_id=project_id, is_delete=False)
        testcases_count = sum([t['testcases_count'] for t in testcases_count])
        configures_count = sum([t['configures_count'] for t in configures_count])
        item["interfaces_count"] = interfaces_count
        item["testsuites_count"] = testsuites_count
        item["testcases_count"] = testcases_count
        item["configures_count"] = configures_count
        data_list.append(item)

    return data_list
