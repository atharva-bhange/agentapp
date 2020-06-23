from django.urls import path 
from .views import index_view, add_agent_view, add_role_view , Agent_list, agent_status_view , add_issue_view

urlpatterns = [
	path('' , index_view , name="index"),
	path('addagent/' , add_agent_view , name="add_agent"),
	path('addrole/' , add_role_view, name="add_role"),
	path('agents/' , Agent_list.as_view(), name="agents"),
	path('agents/<int:aid>/' , agent_status_view, name="change_status"),
	path('addissue/' , add_issue_view, name="add_issue"),
]