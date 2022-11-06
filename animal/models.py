from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class AnimalCategory(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class Meetup(models.Model):
    Meetup_Name  = models.CharField(max_length=500)
    categoryName = models.ForeignKey(AnimalCategory, on_delete=models.CASCADE, related_name='animals')
    venue = models.CharField(max_length=500)
    Date = models.DateTimeField(auto_now=False, auto_now_add=False)
    


    def __str__(self):
        return self.Meetup_Name
    
    def get_absolute_url(self):
    
        return reverse('meetup')

 