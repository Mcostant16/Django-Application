from django.urls import path
from . import views

app_name = "myProfile"
urlpatterns = [ 
	path("", views.image_upload_view, name="index"),
	path("images", views.display_photos, name="images"),
	path("delete_photo/<int:pk>/", views.delete_photo, name="delete_photo"),
	]
	


