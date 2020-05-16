from django.urls import path
from . import views

urlpatterns = [
    path("", views.myProjects_page, name="my_projects_page"),
    path("<int:pk>/", views.detailsOfProject, name="details_of_project"),
]
