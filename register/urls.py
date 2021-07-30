from django.urls import path
from . import views

app_name = "myProfile"
urlpatterns = [ 
	path("upload/", views.image_upload_view, name="upload")
]
	


