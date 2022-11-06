from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=500)
    animal = models.CharField(max_length=500)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now=True)
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return str(self.name)
    
