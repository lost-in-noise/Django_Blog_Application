from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view
    path('create-and-filter-posts/', views.create_and_filter_posts, name='create_and_filter_posts'),  # Path for creating and filtering posts
]
