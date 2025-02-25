from django.contrib import admin
from .models import CreationUserModel
# Register your models here.
class UserCreateAdmin(admin.ModelAdmin):
    model = CreationUserModel
    list_display = ['last_name','cod','ruc',] 

admin.site.register(CreationUserModel,UserCreateAdmin)
