""" Defining url patterns for app """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('planner/', views.planner, name='planner'),
    path('meal_time/<int:day_id>/', views.meal_time, name='meal_time'),
]