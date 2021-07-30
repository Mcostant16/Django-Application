from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Tasks(models.Model):
	task_name = models.CharField(max_length=100)
	priority = models.IntegerField(default=1)
	date_created=models.DateTimeField(default=datetime.now)
	date_updated=models.DateTimeField(auto_now=True)
	# This field is required.
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
  
	def __str__(self): 
		return self.task_name



