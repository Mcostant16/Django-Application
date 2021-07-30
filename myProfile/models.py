from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=False)
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
	
	def __str__(self):
		return self.title

	def delete(self, *args, **kwargs):
		self.image.delete()
		super().delete(*args, **kwargs)