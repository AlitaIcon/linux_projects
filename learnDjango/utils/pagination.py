#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @Time    : 2019/10/22 9:44
# @Author  : icon
# @File    : pagination.py
from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    # page_query_param = 'p'
    page_size_query_param = 'size'
    # page_size = 2
    max_page_size = 50
    page_query_description = '第几页'
    page_size_query_description = '每页几条'

    def get_paginated_response(self, data):
        response = super(PageNumberPaginationManual, self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        response.data['current_page_num'] = self.page.number
        return response
