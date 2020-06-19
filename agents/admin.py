from django.contrib import admin
from .models import Agents, Roles, Agent_role

# Register your models here.

class AgentsAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_available', 'available_since' )


class RolesAdmin(admin.ModelAdmin):
    list_display = ('id','role')


class Agent_roleAdmin(admin.ModelAdmin):
    list_display = ('id','agent', 'role')



admin.site.register(Agents , AgentsAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Agent_role, Agent_roleAdmin)
