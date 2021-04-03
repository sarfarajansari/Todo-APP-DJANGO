from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="index"),
    path("delete/",views.delete_task,name="delete"),
    path("task/completed/",views.completed,name="completed")
]