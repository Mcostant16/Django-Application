from django import forms
from django.forms import ClearableFileInput
from .models import Image


class ImageForm(forms.ModelForm):
	#Form for the image model
	class Meta:
		model = Image
		fields = ('title', 'image')
		widgets = {'image': ClearableFileInput(attrs={'multiple': True}),}