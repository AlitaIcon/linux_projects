#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/10/22 9:44
# @Author  : icon
# @File    : pagination.py
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = 'page_size'
    page_size = 2
    max_page_size = 50
