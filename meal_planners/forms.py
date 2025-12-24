from django import forms
from .models import Day, MealTime, Meal

class DayForm(forms.ModelForm):
    """ This class will create a form for the day model """

    class Meta:
        """ Specifying which fields are allowed and labels """
        model = Day
        fields = ['text']
        labels = {'text':''}


class MealTimeForm(forms.ModelForm):
    """ This class will create a form for the meal time """

    class Meta:
        """ Specifying which fields are allowed and labels """
        model = MealTime
        fields = ['text']
        labels = {'text':''}


class MealForm(forms.ModelForm):
    """ This class will create a form for the meal """

    class Meta:
        """ Specifying which fields are allowed and labels """
        model = Meal
        fields= ['text']
        labels = {'text':''}