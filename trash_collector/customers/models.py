from django.db import models
from django.db.models.fields import DateField
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    pickup_day = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    balance = models.IntegerField()
    onetime_pickup = models.DateField()
    suspension_start = models.DateField()
    suspension_end = models.DateField()

