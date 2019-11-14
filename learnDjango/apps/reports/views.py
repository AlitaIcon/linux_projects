# Create your views here.
import json
import os
import re

from django.http.response import StreamingHttpResponse
from django.utils.encoding import escape_uri_path
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from learnDjango.settings import REPORT_DIR
from reports.utils import format_output, get_file_contents
from reports.models import Reports
from reports.serializer import ReportsModelSerializer
from users.serializer import UserInfoSerializer
from utils.summary import get_summary


class ReportsViewSet(ModelViewSet):
    """
     list:
     返回报告（多个）列表数据

     create:
     创建报告

     retrieve:
     返回报告（单个）详情数据

     update:
     更新（全）报告

     partial_update:
     更新（部分）报告

     destroy:
     删除报告

     names:
     返回所有报告ID和名称
     """
    queryset = Reports.objects.all()
    serializer_class = ReportsModelSerializer
    ordering_fields = ('id', 'name')
    filterset_fields = ['id', 'name']
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_delete = True
        instance.save()

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        res.data["results"] = format_output(res.data.get("results"))
        res.data["count"] = Reports.objects.filter(is_delete=False).count()
        return res

    @action(detail=True)
    def download(self, request, pk=None):
        instance = self.get_object()
        html = instance.html
        name = instance.name
        # match = re.search(r'(.*)_\d+', name)
        # if match:
        #     match = match.group(1)

        # report_path = os.path.join(REPORT_DIR, name+'.html')
        # with open(report_path, encoding='utf-8', mode='w+') as f:
        #     f.write(html)
        # response = StreamingHttpResponse(get_file_contents(report_path))
        response = StreamingHttpResponse(html)
        report_name = escape_uri_path(name)
        response['Content-Type'] = "application/octet-stream"
        response['Content-Disposition'] = "attachment; filename*=UTF-8''{}".format(report_name)
        return response

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        try:
            response.data['summary'] = json.loads(response.data['summary'], encoding='utf-8')
        except Exception as e:
            pass
        return response


class SummaryView(GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        response = {
            'user': UserInfoSerializer(request.user).data,
            'statistics': get_summary()
        }
        return Response(response)
