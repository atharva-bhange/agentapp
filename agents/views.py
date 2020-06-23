from django.shortcuts import render, HttpResponse, redirect
from .forms	 import AddAgentForm , AddRoleForm, AddAgentRole , AddIssueForm
from .models import Agents, Agent_role, Roles, Issues
from django.views.generic import ListView


# Create your views here.

def index_view(request):


	m = request.GET.get('m')
	method = m
	
	if method == None:
		method = 2

	## Getting all agent information
	info = []

	agents = Agents.objects.all().order_by('is_available', 'available_since').reverse()

	for each_agent in agents:
		roles = Agent_role.objects.all().filter(agent = each_agent)
		info.append({
			'id' : each_agent.id,
			'name' : each_agent.name,
			'is_available' : each_agent.is_available,
			'available_since' : each_agent.available_since,
			'roles' : roles
			})

	## Getting all issues information 

	issues = Issues.objects.all().order_by('start_time')
	

	context ={
		'method' : method,
		'agent_info' : info,
		'issues_info' : issues
		}
		
	return render(request , 'agents/index.html', context)
	
	

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

def add_issue_view(request):
	if request.method == 'POST':
		issue_form = AddIssueForm(request.POST)
		if issue_form.is_valid():

			issue_form.save()
			return redirect('index')

		else:

			issue_form = AddIssueForm(request.POST)
			context = {
				'form' : issue_form
			}

			return render(request , 'agents/add_issue.html' , context)

	else:
		issue_form = AddIssueForm()

		context = {
		'form' : issue_form
		}

	return render(request , 'agents/add_issue.html' , context)