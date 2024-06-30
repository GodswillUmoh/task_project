# tasks/urls.py

from django.urls import path
from . import views
from . import api_views  # Import the api_views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/<int:pk>/', views.task_detail, name='task_detail'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('api/tasks/<status>/', api_views.task_list_by_status, name='task_list_by_status'),  
     path('accounts/profile/', views.profile, name='profile'),  
]

