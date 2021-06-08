from django.db import models
from django.db.models.fields import DateField
# Create your models here.

# TODO: Finish customer model by adding necessary properties to fulfill user stories


class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    pickup_day = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    balance = models.IntegerField(null=True)
    onetime_pickup = models.DateField(null=True)
    suspension_start = models.DateField(null=True)
    suspension_end = models.DateField(null=True)
    last_completed_pickup = models.DateField(null=True)

