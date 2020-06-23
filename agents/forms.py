from django.forms import ModelForm
from .models import Agents , Roles, Agent_role, Issues
from bootstrap_datepicker_plus import DateTimePickerInput



class AddAgentForm(ModelForm):

	class Meta():
		model = Agents
		fields = ['name' , 'is_available' , 'available_since']
		widgets = {
			'available_since' : DateTimePickerInput()
        }


class AddRoleForm(ModelForm):

	class Meta():
		model = Roles
		fields = ['role']

class AddAgentRole(ModelForm):

	class Meta():
		model = Agent_role
		fields = ['role']

class AddIssueForm(ModelForm):

	class Meta():
		model = Issues
		fields = ['issue' , 'start_time']
		widgets = {
			'start_time' : DateTimePickerInput()
        }
