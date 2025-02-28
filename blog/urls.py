from django.urls import path
from . import views

uurlpatterns = [
   path("", views.post_list, name="post_list"),

]