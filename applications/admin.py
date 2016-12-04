# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group, Permission
from applications.models import Requester, Supervisor

class RequesterAdmin(admin.ModelAdmin):
    model = Requester

class SupervisorAdmin(admin.ModelAdmin):
    model = Supervisor

admin.site.unregister(Group)
admin.site.register(Requester, RequesterAdmin)
admin.site.register(Supervisor, SupervisorAdmin)
admin.site.site_header = 'CTGS Administration'