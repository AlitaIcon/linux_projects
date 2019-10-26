# Generated by Django 2.2.5 on 2019-10-15 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='项目名称', max_length=300, verbose_name='项目名称')),
                ('leader', models.CharField(help_text='项目负责人', max_length=300, verbose_name='项目负责人')),
                ('des', models.TextField(blank=True, help_text='项目描述', null=True, verbose_name='项目描述')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 's_projects',
            },
        ),
    ]
