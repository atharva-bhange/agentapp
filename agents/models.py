from django.db import models

# Create your models here.

class Agents(models.Model):
	name = models.CharField(max_length = 20, null = True, blank = True)
	is_available = models.BooleanField(null = False, blank = False)	
	available_since = models.DateTimeField()
	no_roles = models.IntegerField(null = True , blank = True)

	class Meta:
		verbose_name_plural = "Agents"

	def __str__(self):
		return str(self.name)


class Roles(models.Model):
	role = models.CharField(max_length = 128)

	class Meta:
		verbose_name_plural = "Roles"
	
	def __str__(self):
		return str(self.role)

class Agent_role(models.Model):
	agent = models.ForeignKey(Agents , on_delete=models.CASCADE)
	role = models.ForeignKey(Roles , on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Agent_role"

class Issues(models.Model):
	issue = models.CharField(max_length = 20, null = True, blank = True)
	start_time = models.DateTimeField()
	no_roles = models.IntegerField(null = True , blank = True)

	class Meta:
		verbose_name_plural = "Issues"

class Issue_role(models.Model):
	issue = models.ForeignKey(Issues , on_delete=models.CASCADE)
	role = models.ForeignKey(Roles , on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = "Issue_role"






	