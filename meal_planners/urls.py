""" Defining url patterns for app """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('planner/', views.planner, name='planner'),
    path('meal_time/<int:day_id>/', views.meal_time, name='meal_time'),
    path('add_day/', views.add_day, name='add_day'),
    path('add_meal_time/<int:day_id>/', views.add_meal_time, name='add_meal_time'),
    path('add_meal/<int:meal_time_id>/', views.add_meal, name='add_meal'),
]