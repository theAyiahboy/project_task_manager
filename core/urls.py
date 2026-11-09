from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/create/", views.create_project, name="create_project"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("projects/<int:project_id>/tasks/create/",views.create_task,name="create_task"),
    path("projects/<int:project_id>/edit/",views.edit_project,name="edit_project"),
    path("projects/<int:project_id>/delete/",views.delete_project,name="delete_project"),
    path("tasks/<int:task_id>/edit/",views.edit_task,name="edit_task"),
    path("tasks/<int:task_id>/delete/",views.delete_task,name="delete_task"),
]  
