from django.db import models


class Day(models.Model):
    """ This class handles the text day """

    text = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
    

class MealTime(models.Model):
    """ This class handles the text meal time """

    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    text = models.CharField(max_length=30)

    def __str__(self):
        return self.text
    

class Meal(models.Model):
    """ This class handles the text meal """

    meal_time = models.ForeignKey(MealTime, on_delete=models.CASCADE)
    text = models.CharField(max_length=90)

    def __str__(self):
        return self.text
