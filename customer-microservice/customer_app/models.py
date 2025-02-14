from django.db import models
from django.utils import timezone


class Customer(models.Model):
    cvid = models.AutoField(primary_key=True)
    ccname = models.CharField(max_length=100,  blank=False, null=False)
    ccemail = models.CharField(max_length=100, unique=True,blank=False, null=False)
    cvbalance = models.DecimalField(max_digits=18, decimal_places=2, blank=False, null=False, default=0.00)
    cvcreatedate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cvname

class CustomerChargeLog(models.Model):
    cvid = models.AutoField(primary_key=True)
    cvvalue = models.DecimalField(max_digits=18, decimal_places=2)
    cvidcustomer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    cvcreatedate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Charge {self.cvid} for Customer {self.cvidcustomer.cvname}"

class Penalty(models.Model):
    cvid = models.AutoField(primary_key=True)
    cvscheduleid = models.IntegerField(blank=False, null=False)
    cvdaysdelayed = models.IntegerField(blank=False, null=False, default=0)
    cbpayed = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.cvid
