#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/11/13 17:43
# @Author  : icon
# @File    : summary.py
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
    sta["projects_count"] = Projects.objects.all().count()
    sta["interfaces_count"] = Interfaces.objects.all().count()
    sta["testcases_count"] = TestCases.objects.all().count()
    sta["testsuites_count"] = TestSuites.objects.all().count()
    sta["configures_count"] = Configures.objects.all().count()
    sta["envs_count"] = Envs.objects.all().count()
    sta["debug_talks_count"] = DebugTalks.objects.all().count()
    sta["reports_count"] = Reports.objects.all().count()
    sta["success_rate"] = round((Reports.objects.filter(result=True).count() / sta["reports_count"]) * 100, 1)
    sta["fail_rate"] = round((Reports.objects.filter(result=False).count() / sta["reports_count"]) * 100, 1)
    return sta
