from django.test import TestCase , Client
from django.urls import reverse
from agents.models import Agents , Roles, Issues, Agent_role , Issue_role
import json


class TestView(TestCase):

	## Only GET method is done

	def setUp(self):
		self.client = Client()
		self.index_url = reverse('index')
		self.add_agent_url = reverse('add_agent')
		self.add_role_url = reverse('add_role')
		# self.agent_1 = Agents(
		# 	name = 'bla',
		# 	is_available = False,
		# 	available_since = '06/25/2020 00:18',
		# 	no_roles = 1
		# 	)
		self.Agent_list_url = reverse('agents')
		self.add_issue_url = reverse('add_issue')

	def test_index_view_GET(self):

		response = self.client.get(self.index_url)

		self.assertEquals(response.status_code , 200)
		self.assertTemplateUsed(response , 'agents/index.html')


	def test_add_agent_view_GET(self):

		response = self.client.get(self.add_agent_url)

		self.assertEquals(response.status_code , 200)
		self.assertTemplateUsed(response , 'agents/add_agent.html')

	def test_add_role_view_GET(self):

		response = self.client.get(self.add_role_url)

		self.assertEquals(response.status_code , 200)
		self.assertTemplateUsed(response , 'agents/add_role.html')		

	def test_Agent_list_view_GET(self):

		response = self.client.get(self.Agent_list_url)

		self.assertEquals(response.status_code , 200)
		self.assertTemplateUsed(response , 'agents/agents.html')

	def test_add_issue_view_GET(self):

		response = self.client.get(self.add_issue_url)

		self.assertEquals(response.status_code , 200)
		self.assertTemplateUsed(response , 'agents/add_issue.html')	

	# def test_add_agent_view_POST(self):

	# 	role = Roles(role = 'product')

	# 	self.client.post(self.add_agent_url , {
	# 		'name' : 'bla',
	# 		'is_available' : False,
	# 		'available_since' : '06/25/2020 00:18',
	# 		'form-0-role' : role,
	# 		'form-TOTAL_FORMS' : 1,
	# 		'form-INITIAL_FORMS' : 0,
	# 		'form-MIN_NUM_FORMS' : 0,
	# 		'form-MAX_NUM_FORMS' : 1000
	# 		})	

	# 	self.assertEquals(response.status_code , 302)
	# 	self.assertTrue(Agents.objects.filter(name = 'bla').exists())

