import random

def select_agent(mode , Agents , Issues , Agent_role , Issue_role):
	# Function Defination 


	if mode == 1:
		# All Available

		## Issue agent list
		issue_agent_list = []

		issues = Issues.objects.all().order_by('start_time')
		available_agents = Agents.objects.all().filter(is_available = True)

		for each_issue in issues:
			temp = {}
			required_roles = Issue_role.objects.filter(issue = each_issue)
			required_roles_id = []
			for required_role in required_roles:
				required_roles_id.append(required_role.role.id)
	
			#print(each_issue.issue)
			temp['id'] = each_issue

			## Loading agent with respect to each issue
			agent_list = []
			for each_available_agent in available_agents:

				available_agent_roles = Agent_role.objects.filter(agent = each_available_agent)
				available_agent_roles_id = []
				for available_agent_role in available_agent_roles:
					available_agent_roles_id.append(available_agent_role.role.id)
				

				#print(required_roles_id , available_agent_roles_id)
				if set(required_roles_id).issubset(set(available_agent_roles_id)):
					
					agent_list.append(each_available_agent)

			temp['agents'] = agent_list

			issue_agent_list.append(temp)


		return issue_agent_list
		
	elif mode == 2:
		# Least Busy

		## Issue agent list
		issue_agent_list = []

		issues = Issues.objects.all().order_by('start_time')
		available_agents = Agents.objects.all().filter(is_available = True).order_by('available_since')

		for each_issue in issues:
			temp = {}
			required_roles = Issue_role.objects.filter(issue = each_issue)
			required_roles_id = []
			for required_role in required_roles:
				required_roles_id.append(required_role.role.id)
	
			#print(each_issue.issue)
			temp['id'] = each_issue

			## Loading agent with respect to each issue
			agent_list = []
			for each_available_agent in available_agents:

				available_agent_roles = Agent_role.objects.filter(agent = each_available_agent)
				available_agent_roles_id = []
				for available_agent_role in available_agent_roles:
					available_agent_roles_id.append(available_agent_role.role.id)
				

				#print(required_roles_id , available_agent_roles_id)
				if set(required_roles_id).issubset(set(available_agent_roles_id)):
					agent_list.append(each_available_agent)
					break

			temp['agents'] = agent_list

			issue_agent_list.append(temp)


		return issue_agent_list

	elif mode == 3:
		# Random

		## Issue agent list
		issue_agent_list = []

		issues = Issues.objects.all().order_by('no_roles')
		available_agents = Agents.objects.all().filter(is_available = True).order_by('no_roles')

		## Making main agent list
		main_agent_list = []
		for agent in available_agents:
			main_agent_list.append(agent)

		for each_issue in issues:
			temp = {}

			required_roles = Issue_role.objects.filter(issue = each_issue)
			required_roles_id = []

			for required_role in required_roles:
				required_roles_id.append(required_role.role.id)

			temp['id'] = each_issue

			agent_list = []
			for each_agent in main_agent_list:
				available_agent_roles = Agent_role.objects.filter(agent = each_agent)
				available_agent_roles_id = []
				for available_agent_role in available_agent_roles:
					available_agent_roles_id.append(available_agent_role.role.id)


				if set(required_roles_id).issubset(set(available_agent_roles_id)):
					agent_list.append(each_agent)
			if len(agent_list) == 0:
				temp['agent'] = []
			else:
				choosen_agent = random.choice(agent_list)
				temp['agents'] = [choosen_agent]
				main_agent_list.remove(choosen_agent)

			issue_agent_list.append(temp)

		return issue_agent_list

	else:
		# Incorrect argument
		return None

	return None