import json

from django.db.models import Q, Count
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views import View
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from projects.models import Projects
from projects.serializer import ProjectModelSerializer, InterfaceByProjectsIdSerializer


def index(request):
    if request.method == "GET":
        # return HttpResponse('<h1>hello</h1>')
        datas = [
            {"name": "项目A"},
            {"name": "项目B"},
            {"name": "项目C"},
        ]
        return render(request, 'demo.html', locals())

    return HttpResponse('<h1>not get method</h1>')


class Hello(View):
    # def get(self, request, pk):
    def get(self, request):
        # return render(request, 'demo.html')
        data = {
            "name": "admin",
            "age": 18
        }
        print(request.body)
        # return HttpResponse(f'<h1>not get method,{request.path_info},{pk}</h1>')
        # return HttpResponse(content=json.dumps(data), content_type='application/json', status=201)
        return JsonResponse(data=data, status=201)

    def post(self, request):
        """发送json，请求解码"""
        r = request.body.decode()
        res = json.loads(r)
        return HttpResponse(f'<h1>{res}</h1>')


class DataDemo(View):
    def get(self, request):
        # 新增
        # 方法1
        p = Projects(name='app项目3', leader='test', des='app项目')
        p.save()
        # 方法2
        Projects.objects.create(name='小程序项目', leader='test', des='小程序项目')

        # 查询
        # 排序查询
        Projects.objects.filter(id__gt=3).order_by('name')
        Projects.objects.all().order_by('-id')
        Projects.objects.all().order_by('name', '-id')
        # 或查询
        Projects.objects.filter(Q(id=3) | Q(id=4))
        # 与查询
        Projects.objects.filter(name__contains='小', leader='test')
        Projects.objects.filter(name__contains='小').filter(leader='test')
        # 分组查询，聚合函数查询
        Projects.objects.all().values("leader").annotate(leader_num=Count("leader"))
        # 关联查询
        # 通过父表查询子表的信息
        Projects.objects.filter(interface__name='login').first()

        # 指定字段更新
        Projects.objects.filter(pk=1).update(name='小程序项目2')
        # 更新部分字段，但是会更新所有
        qs_u = Projects.objects.filter(id=2)
        qs_u.name = 'update'
        qs_u.save()

        # 删除
        Projects.objects.filter(id=1).delete()
        return HttpResponse('success')


class GetProjects(APIView):
    def get(self, request):
        p_obj = Projects.objects.all()
        # return JsonResponse({
        #     "data": {"projects": [{"name": p.name, "leader": p.leader, "des": p.des}for p in p_obj]},
        #     "msg": "all projects"
        # })
        return JsonResponse([{"name": i.name} for i in p_obj], safe=False)


class ProjectsViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectModelSerializer
    ordering_fields = ['name']
    filterset_fields = ['id', 'name']

    @action(methods=['get'], detail=True, url_path='interfaces')  # detail=True，那么路由前面会有id
    def interfaces(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = InterfaceByProjectsIdSerializer(instance=instance)
        return Response(serializer.data)
