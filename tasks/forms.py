from django import forms
from .models import Tasks
# Create your views here.

class NewTaskForm(forms.ModelForm):
	class Meta:
		model = Tasks
		fields =  ["task_name","priority" ]