#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/6 21:06
# @Author  : icon
# @File    : utils.py
from interfaces.models import Interfaces
from testcases.models import TestCases


def get_count_by_project(datas):
    data_list = []
    for item in datas:
    # match = re.search(r'(.*)T(.*)\..*?', item['create_time'])
    # item['create_time'] = match.group(1) + " " + match.group(2)
        data_list.append(item)

    return data_list


def get_testcases_by_interface_ids(ids_list):
    """
    通过接口id获取用例
    :param ids_list:
    :return:
    """
    one_list = []
    for interface_id in ids_list:
        # testcases_qs = TestCases.objects.values_list('id', flat=True).\
        #     filter(interface_id=interface_id, is_delete=False)
        testcases_qs = [i.id for i in Interfaces.objects.get(is_delete=False, id=interface_id).testcases.all()]
        one_list.extend(list(testcases_qs))
    return one_list
