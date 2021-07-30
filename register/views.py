from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib import messages 
from django.contrib.auth import logout, authenticate, login
# Create your views here.

def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(response, f"New Account Created: {username}")
			return redirect("/projects")
		
		else:
			for msg in form.error_messages:
				messages.error(response, f"{msg}: {form.error_messages[msg]}")
	else:
		form = RegisterForm()
	
	return render(response, "register/register.html", {"form":form})
	
def logout_request(response):
	logout(response)
	messages.info(response, "Logged out succesfully!")
	return redirect("/projects")

def login_request(response):
	if response.method == "POST":
		form = LoginForm(response, data=response.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(response, user)
				messages.success(response, f"Your are now logged in as: {username}")
				return redirect("/projects")
			else:
				messages.error(response, "Invalid username or password")
		else:
			messages.error(response, "Invalid username or password")
		
			
	form = LoginForm()
	return render(response,"login/login.html",{"form":form})
	
	

