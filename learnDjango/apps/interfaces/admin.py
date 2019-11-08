from django.contrib import admin

# Register your models here.
from .models import Interfaces


class InterfaceAdmin(admin.ModelAdmin):
    # fields = ('name', 'leader', 'des')
    list_display = ['id', 'name', 'project_id', 'tester', 'desc']
    list_display_links = ('id', 'name')


admin.site.register(Interfaces, InterfaceAdmin)