#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/13 17:43
# @Author  : icon
# @File    : summary.py
from django.db.models import Sum

from configures.models import Configures
from debugtalks.models import DebugTalks
from envs.models import Envs
from interfaces.models import Interfaces
from projects.models import Projects
from reports.models import Reports
from testcases.models import TestCases
from testsuites.models import TestSuites


def get_summary():
    sta = dict()
    sta["projects_count"] = Projects.objects.filter(is_delete=False).count()
    sta["interfaces_count"] = Interfaces.objects.filter(is_delete=False).count()
    sta["testcases_count"] = TestCases.objects.filter(is_delete=False).count()
    sta["testsuites_count"] = TestSuites.objects.filter(is_delete=False).count()
    sta["configures_count"] = Configures.objects.filter(is_delete=False).count()
    sta["envs_count"] = Envs.objects.filter(is_delete=False).count()
    sta["debug_talks_count"] = DebugTalks.objects.filter(is_delete=False).count()
    sta["reports_count"] = Reports.objects.filter(is_delete=False).count()
    run_testcases_success_count = Reports.objects.filter(is_delete=False).aggregate(Sum('success'))['success__sum'] or 0
    run_testcases_total_count = Reports.objects.filter(is_delete=False).aggregate(Sum('count'))['count__sum'] or 0
    if run_testcases_total_count:
        sta["success_rate"] = round((run_testcases_success_count / run_testcases_total_count) * 100, 1)
        sta["fail_rate"] = round(100 - sta["success_rate"], 1)
    else:
        sta["success_rate"] = 0
        sta["fail_rate"] = 0
    return sta
