from django.db import models

# Create your models here.

class Agents(models.Model):
	name = models.CharField(max_length = 20, null = True, blank = True)
	is_available = models.BooleanField(null = False, blank = False)	
	available_since = models.DateTimeField()

	def __str__(self):
		return self.name


class Roles(models.Model):
	role = models.CharField(max_length = 128)
	
	def __str__(self):
		return self.role

class Agent_role(models.Model):
	agent = models.ForeignKey(Agents , on_delete=models.CASCADE)
	role = models.ForeignKey(Roles , on_delete=models.CASCADE)






	