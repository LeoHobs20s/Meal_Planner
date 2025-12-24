from django.shortcuts import render, get_object_or_404
from .models import Day

def home(request):
    """ This view will render the home page """
    return render(request, 'meal_planners/home.html')


def planner(request):
    """ This view will render the full meal planner page """

    days = Day.objects.all()
    context = {'days':days}
    return render(request, 'meal_planners/planner.html', context)


def meal_time(request, day_id):
    """ This view will render the meal times """

    day = get_object_or_404(Day, pk=day_id)
    meal_times = day.mealtime_set.all()
    context = {'day':day, 'meal_times': meal_times}
    return render(request, 'meal_planners/day_meal_plan.html', context)


