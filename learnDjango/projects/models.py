from django.db import models


# Create your models here.


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)


class Projects(models.Model):
    name = models.CharField(verbose_name='项目名称', max_length=300, help_text='项目名称')
    leader = models.CharField(verbose_name='项目负责人', max_length=300, help_text='项目负责人')
    # null：True表示空值被存储为NULL， blank：True表示该字段可不传
    des = models.TextField(verbose_name='项目描述', help_text='项目描述', null=True, blank=True)

    class Meta:
        db_table = 's_projects'
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name


