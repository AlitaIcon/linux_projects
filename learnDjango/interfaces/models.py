from django.db import models

# Create your models here.

from projects.models import Projects


class Interface(models.Model):
    name = models.CharField(verbose_name='接口名称', max_length=200, help_text='接口名称')
    url = models.CharField(verbose_name='接口地址', max_length=100, unique=True, help_text='接口地址')
    data = models.CharField(verbose_name='参数', max_length=100, help_text='接口参数', null=True, blank=True)
    projects = models.ForeignKey(Projects, on_delete=models.CASCADE, verbose_name='所属项目', help_text='所属项目')

    class Meta:
        ordering = ['name']
        verbose_name = '接口模块'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
