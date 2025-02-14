from datetime import date

from django.db import models


class Schedule(models.Model):
    cvid = models.AutoField(primary_key=True)  
    cvcustomerid = models.IntegerField(null=False, blank=False)  
    cdwithdrawdate = models.DateField(null=True, blank=True, default=date.today())
    cdduedate = models.DateField(null=False, blank=False)  
    cdreturneddate = models.DateField(null=True, blank=True)
    cvvalue = models.DecimalField(max_digits=18, decimal_places=2, default=0)  
    cdcreatedate = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Returned date: {self.cdreturneddate}, Due date: {self.cdduedate}"

class Association(models.Model):
    cvid = models.AutoField(primary_key=True)  
    cvproductid = models.IntegerField(null=False, blank=False)
    cvscheduleid = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return f"Association {self.cvid} - Product {self.cvproductid}"
