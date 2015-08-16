from django.db import models

# Create your models here.
class Address(models.Model):
    office = models.CharField(max_length = 50)
    pincode = models.CharField(max_length = 6)
    division = models.CharField(max_length = 50)
    region = models.CharField(max_length = 50)
    circle = models.CharField(max_length = 100)
    taluk = models.CharField(max_length = 100)
    district = models.CharField(max_length = 50)
    state = models.CharField(max_length = 100)
    created_on = models.DateTimeField(auto_now_add = True)
    updated_on  = models.DateTimeField(auto_now =True)