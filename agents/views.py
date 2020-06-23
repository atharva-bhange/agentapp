from django.shortcuts import render, HttpResponse, redirect
from .forms	 import AddAgentForm , AddRoleForm, AddAgentRole
from .models import Agents, Agent_role, Roles
from django.views.generic import ListView


# Create your views here.

def index_view(request):
	return render(request , 'agents/index.html')

def add_agent_view(request):
	if request.method == 'POST':
		agent_form = AddAgentForm(request.POST)
		if agent_form.is_valid():

			agent = agent_form.save()
			

			agent_role = Agent_role()
			agent_role.agent = agent
			agent_role.role = Roles.objects.get(id = request.POST['role'])

			agent_role.save()

			return redirect('index')

		else:

			agent_form = AddAgentForm(request.POST)
			context = {
				'form' : agent_form
			}

			return render(request , 'agents/add_agent.html' , context)

	else:
		agent_form = AddAgentForm()
		role_form = AddAgentRole()


		context = {
		'form' : agent_form,
		'role' : role_form
		}

	return render(request , 'agents/add_agent.html' , context)


def add_role_view(request):

	if request.method == 'POST':

		role_form = AddRoleForm(request.POST)
		if role_form.is_valid():

			role_form.save()
			return redirect('index')

		else:

			agent_form = AddRoleForm(request.POST)
			context = {
				'form' : role_form
			}
				
			return render(request , 'agents/add_role_view.html' , context)
	else:
		role_form = AddRoleForm()

		context = {
		'form' : role_form
		}

	return render(request , 'agents/add_role.html', context)


def agent_status_view(request , aid):
	agent_id = aid
	agent = Agents.objects.get(id=aid)


	if request.method == 'POST':
		agent_form = AddAgentForm(request.POST , instance = agent)
		if agent_form.is_valid():

			agent_form.save()
			return redirect('index')

		else:

			agent_form = AddAgentForm(request.POST)
			context = {
				'form' : agent_form
			}

			return render(request , 'agents/add_agent.html' , context)

	else:
		agent_form = AddAgentForm(instance = agent)

		context = {
		'form' : agent_form
		}

	return render(request , 'agents/edit_agent.html' , context)


	# return render(request , 'agents/change_status.html')



class Agent_list(ListView):
    context_object_name = 'agents'
    model = Agents
    template_name = 'agents/agents.html'