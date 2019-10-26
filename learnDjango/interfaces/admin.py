from django.contrib import admin

# Register your models here.
from .models import Interface


class InterfaceAdmin(admin.ModelAdmin):
    # fields = ('name', 'leader', 'des')
    list_display = ['id', 'name', 'url', 'data', 'projects']
    list_display_links = ('id', 'name')


admin.site.register(Interface, InterfaceAdmin)