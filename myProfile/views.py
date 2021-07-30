from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required

def image_upload_view(request):
    #Process images uploaded by users
	if request.method == 'POST':
		form = ImageForm(request.POST,request.FILES)
		if form.is_valid():
			fs = form.save(commit=False)
			for file in request.FILES.getlist('image'):
				fs.pk = None
				fs.image = file
				fs.user = request.user
				fs.save()
			# Get the current instance object to display in the template
			img_obj = form.instance
			return render(request, 'myProfile/index.html', {'form': form, 'img_obj': img_obj})
		else: 
			form = ImageForm()
			return render(request, 'myProfile/index.html', {'form': form})
	else:
		form = ImageForm()
		return render(request, 'myProfile/index.html', {'form': form})
	
def display_photos(request): 
	if request.method == 'GET': 
	# getting all the objects of hotel. 
		user_images = Image.objects.filter(user=request.user)
		#context = {"tasks" : query_results}
		#allImages = Image.objects.all()  
		return render(request, 'myProfile/allimages.html',{'images' : user_images})

def delete_photo(request, pk): 
	if request.method == 'POST':
		image = Image.objects.get(id=pk) 
		image.delete() 
		messages.info(request, "Image removed !!!") 
	return redirect(reverse('myProfile:images'))
	#return redirect('index')
