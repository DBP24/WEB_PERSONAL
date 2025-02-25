from django.contrib import admin
from .models import ExperienciaModel,StudyModel,CapacityModel,ProjectModel
# Register your models here.

class ExperienciaModelAdmin(admin.ModelAdmin):
    list_display= ('company_name', 'rol', 'start_date', 'end_date', 'description')


class StudyModelAdmin(admin.ModelAdmin):
    list_display= ('ie',)

class CapacityModelAdmin(admin.ModelAdmin):
    list_display= ('ie',)
    ordering = ['start_date']
    list_filter = ('start_date',)

class ProjectModelAdmin(admin.ModelAdmin):
    list_display= ('name',)
  


admin.site.register(ExperienciaModel, ExperienciaModelAdmin)
admin.site.register(StudyModel, CapacityModelAdmin)
admin.site.register(CapacityModel, CapacityModelAdmin)
admin.site.register(ProjectModel, ProjectModelAdmin)