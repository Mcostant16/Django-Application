from django.urls import path
from . import views

app_name = "tasks"
urlpatterns = [ 
	path("", views.index, name="index"),
	path("add", views.add, name="add"),
	####################give id no. item_id name or item_id=i.id ############ 
    path("del/<int:pk>/", views.remove, name="del")
]
	


