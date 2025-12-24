from django.shortcuts import render
from .models import Day

def home(request):
    """ This view will render the home page """
    return render(request, 'meal_planners/home.html')


def planner(request):
    """ This view will render the full meal planner page """

    days = Day.objects.all()
    context = {'days':days}
    return render(request, 'meal_planners/planner.html', context)