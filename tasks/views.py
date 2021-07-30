from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Tasks
from .forms import NewTaskForm
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
	#query_results = Tasks.objects.all()
	query_results = Tasks.objects.filter(user=request.user)
	context = {"tasks" : query_results}
	return render(request, "tasks/index.html", context)

def add(request):
	if request.method == "POST":
		form = NewTaskForm(request.POST)
		if request.user.is_authenticated and  form.is_valid():
			#task = form.cleaned_data["task"]
			fs=form.save(commit=False)
			fs.user = request.user
			fs.save()
			#context= {'tasks': form}
			return HttpResponseRedirect(reverse("tasks:index"))
			#return render(request, "tasks/index.html", context)
		else:
			messages.info(request, "You need to Login to submit form!!!") 
			return render(request, "tasks/add.html", {
				"form": form
			})
	else:
		return render(request, "tasks/add.html", {
			"form": NewTaskForm()
		})
		

def remove(request, pk): 
    item = Tasks.objects.get(id=pk) 
    item.delete() 
    messages.info(request, "item removed !!!") 
    return HttpResponseRedirect(reverse("tasks:index"))
	#return redirect('index')