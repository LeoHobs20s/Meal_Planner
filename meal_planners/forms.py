from django import forms
from .models import Day

class DayForm(forms.ModelForm):
    """ This class will create a form for the day model """

    class Meta:
        """ Specifying which fields are allowed and labels """

        model = Day
        fields = ['text']
        labels = {'text':''}