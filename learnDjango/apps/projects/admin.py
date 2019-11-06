from django.contrib import admin

# Register your models here.
# from .models import Question
#
# admin.site.register(Question)
from .models import Projects


class ProjectsAdmin(admin.ModelAdmin):
    # fields = ('name', 'leader', 'des')
    list_display = ['id', 'name', 'leader', 'desc']
    list_display_links = ('id', 'name')


admin.site.register(Projects, ProjectsAdmin)
