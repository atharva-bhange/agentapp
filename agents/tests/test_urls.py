from django.test import SimpleTestCase
from django.urls import reverse, resolve
from agents.views import (index_view,
						add_agent_view,
						add_role_view,
						agent_status_view,
						Agent_list,
						add_issue_view)


class TestUrls(SimpleTestCase):

	def test_index_url_is_resolved(self):
		url = reverse('index')
		self.assertEquals(resolve(url).func , index_view)

	def test_add_agent_url_is_resolved(self):
		url = reverse('add_agent')
		self.assertEquals(resolve(url).func , add_agent_view)

	def test_add_role_url_is_resolved(self):
		url = reverse('add_role')
		self.assertEquals(resolve(url).func , add_role_view)

	def test_agents_url_is_resolved(self):
		url = reverse('agents')
		self.assertEquals(resolve(url).func.view_class , Agent_list)

	def test_add_issue_url_is_resolved(self):
		url = reverse('add_issue')
		self.assertEquals(resolve(url).func , add_issue_view)
