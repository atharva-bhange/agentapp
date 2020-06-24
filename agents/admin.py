from django.contrib import admin
from .models import Agents, Roles, Agent_role, Issues, Issue_role

# Register your models here.

class AgentsAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_available', 'available_since','no_roles' )


class RolesAdmin(admin.ModelAdmin):
    list_display = ('id','role')


class Agent_roleAdmin(admin.ModelAdmin):
    list_display = ('id','agent', 'role')

class IssuesAdmin(admin.ModelAdmin):
    list_display = ('id','issue', 'start_time', 'no_roles')

class Issue_roleAdmin(admin.ModelAdmin):
    list_display = ('id','issue', 'role')


admin.site.register(Agents , AgentsAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Agent_role, Agent_roleAdmin)
admin.site.register(Issues, IssuesAdmin)
admin.site.register(Issue_role, Issue_roleAdmin)
