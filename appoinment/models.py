from django.db import models
from django.urls import reverse
# Create your models here.

class Hospital(models.Model):
    hospital = models.CharField(max_length=50)

    def __str__(self):
        return self.hospital


class Patient(models.Model):
    name = models.CharField(max_length=50)
    animal = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    phone = models.IntegerField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    appoinment_date = models.DateField(auto_now=False, auto_now_add=False)
    area = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.PositiveIntegerField()



    def __str__(self):
        return self.name 

    def get_absolute_url(self):
        return reverse("appoinment_pdf",kwargs={"pk": self.pk})
    

    