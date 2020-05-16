from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogsPage, name="blogs_page"),
    path("<int:pk>/", views.detailsOfBlog, name="details_of_blog"),
    path("<category>/", views.blog_category, name="blog_category"),
]
