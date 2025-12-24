from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Day, MealTime
from .forms import DayForm, MealTimeForm, MealForm

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


def add_day(request):
    """ This view will render a form to add a day """

    if request.method != 'POST':
        # No Data Submitted; create a blank form
        form = DayForm()
    else:
        # POST Data Submitted; process data
        form = DayForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('planner'))
    
    context = {'form':form}
    return render(request, 'meal_planners/add_day.html', context)


def add_meal_time(request, day_id):
    """ This view will render the form to add meal time """

    day = get_object_or_404(Day, pk=day_id)
    if request.method != "POST":
        # No Data Submitted; create blank form
        form = MealTimeForm()
    else:
        # POST Data Submitted; process data
        form = MealTimeForm(data=request.POST)
        if form.is_valid():
            new_meal_time = form.save(commit=False)
            new_meal_time.day = day
            new_meal_time.save()
            return HttpResponseRedirect(reverse('meal_time', args=[day_id]))
    
    context = {'day':day, 'form':form}
    return render(request, 'meal_planners/add_meal_time.html', context)


def add_meal(request, meal_time_id):
    """ This view will render the form to add meal """

    meal_time = get_object_or_404(MealTime, pk=meal_time_id)
    day = meal_time.day
    if request.method != 'POST':
        # No Data Submitted; create blank form
        form = MealForm()
    else:
        # POST Data Submitted; process data
        form = MealForm(data=request.POST)
        if form.is_valid():
            new_meal = form.save(commit=False)
            new_meal.meal_time = meal_time
            new_meal.save()
            return HttpResponseRedirect(reverse('meal_time', args=[day.id]))
        
    context = {'meal_time':meal_time, 'form':form}
    return render(request, 'meal_planners/add_meal.html', context)
        