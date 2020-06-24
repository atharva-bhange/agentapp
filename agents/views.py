from django.shortcuts import render, HttpResponse, redirect
from .forms	 import AddAgentForm , AddRoleForm,AddIssueForm
from .models import Agents, Agent_role, Roles, Issues, Issue_role
from django.views.generic import ListView
from django.forms import modelformset_factory
from .function import select_agent

# Create your views here.

def index_view(request):


	m = request.GET.get('m')
	
	
	if m == None:
		mode = 2
	else:
		mode = int(m)

	## Getting all agent information
	agent_info = []

	agents = Agents.objects.all().order_by('is_available', 'available_since').reverse()

	for each_agent in agents:
		roles = Agent_role.objects.all().filter(agent = each_agent)
		agent_info.append({
			'id' : each_agent.id,
			'name' : each_agent.name,
			'is_available' : each_agent.is_available,
			'available_since' : each_agent.available_since,
			'roles' : roles
			})

	## Getting all issues information 
	issue_info = []

	issues = Issues.objects.all().order_by('start_time')

	for each_issue in issues:
		issue_roles = Issue_role.objects.all().filter(issue = each_issue)
		issue_info.append({
			'id' : each_issue.id,
			'issue' : each_issue.issue,
			'start_time' : each_issue.start_time,
			'roles' : issue_roles
			})
	
	## Running the function according to mode
	print(mode)

	issue_agent_list = select_agent(mode , Agents , Issues, Agent_role , Issue_role)

	print(issue_agent_list)

	context ={
		'mode' : str(mode),
		'agent_info' : agent_info,
		'issues_info' : issue_info,
		'issue_agent_list' : issue_agent_list
		}
		
	return render(request , 'agents/index.html', context)
	
	

def add_agent_view(request):
	role_form = modelformset_factory(Agent_role, fields = ('role',))
	if request.method == 'POST':

		agent_form = AddAgentForm(request.POST)
		if agent_form.is_valid():

			agent = agent_form.save(commit = False)
			agent.no_roles = int(request.POST.get('form-TOTAL_FORMS'))
			agent.save()
			
			r_form = role_form(request.POST)
			for role in r_form:
				role.instance.agent = agent

			if r_form.is_valid:
				print("valid")
				r_form.save()
				redirect("index")
			else:
				print("not valid")
				redirect("index")
			return redirect('index')

		else:

			agent_form = AddAgentForm(request.POST)
			context = {
				'form' : agent_form
			}

			return render(request , 'agents/add_agent.html' , context)

	else:
		agent_form = AddAgentForm()

		
		agent_role_form = role_form(queryset=Agent_role.objects.none())

		context = {
		'form' : agent_form,
		'role' : agent_role_form
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
	role_form = modelformset_factory(Issue_role, fields = ('role',))
	if request.method == 'POST':

		issue_form = AddIssueForm(request.POST)
		if issue_form.is_valid():

			issue = issue_form.save()
			issue.no_roles = int(request.POST.get('form-TOTAL_FORMS'))
			issue.save()
			
			r_form = role_form(request.POST)
			for role in r_form:
				role.instance.issue = issue

			if r_form.is_valid:
				print("valid")
				r_form.save()
				redirect("index")
			else:
				print("not valid")
				redirect("index")
			return redirect('index')

		else:

			agent_form = AddAgentForm(request.POST)
			context = {
				'form' : agent_form
			}

			return render(request , 'agents/add_agent.html' , context)

	else:
		issue_form = AddIssueForm()

		
		issue_role_form = role_form(queryset=Issue_role.objects.none())

		context = {
		'form' : issue_form,
		'role' : issue_role_form
		}

	return render(request , 'agents/add_issue.html' , context)	
