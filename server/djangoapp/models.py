# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# Car Make model
class CarMake(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=511)

    def __str__(self):
        return self.name

# Car Model model
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=3, choices={
        'sdn':'Sedan',
        'suv':'SUV',
        'wgn':'Wagon',
        'spr':'Sport',
        'mus':'Muscle'
        }, default='suv')
    year = models.IntegerField()
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str___(self):
        return self.name
