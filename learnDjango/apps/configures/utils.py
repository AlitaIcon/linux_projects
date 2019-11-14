#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/6 21:06
# @Author  : icon
# @File    : utils.py
from configures.models import Configures


def get_count_by_project(datas):
    data_list = []
    for item in datas:
        # match = re.search(r'(.*)T(.*)\..*?', item['create_time'])
        # item['create_time'] = match.group(1) + " " + match.group(2)
        configures_id = item["id"]
        name = item.pop("interface")
        project_name = Configures.objects.get(pk=configures_id).interface.project.name
        item["interface"] = {
            'name': name,
            'project': project_name
        }
        data_list.append(item)

    return data_list





