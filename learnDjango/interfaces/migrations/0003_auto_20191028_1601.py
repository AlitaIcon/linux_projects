# Generated by Django 2.2.5 on 2019-10-28 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interfaces', '0002_auto_20191028_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interface',
            name='name',
            field=models.CharField(db_column='I_NAME', help_text='接口名称', max_length=200, verbose_name='接口名称'),
        ),
    ]