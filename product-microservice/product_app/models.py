
from django.db import models


class Tbproduct(models.Model):
    cvid = models.AutoField(primary_key=True) 
    ccdescription = models.CharField(max_length=100, unique=True, blank=False, null=False) 
    cvamount = models.IntegerField(default=0) 
    ccproducttype = models.CharField(max_length=50, blank=False, null=False) 

    @property
    def id(self):
        return self.cvid
    
    def __str__(self):
        return self.description


class Tbfavorite(models.Model):
    cvid = models.AutoField(primary_key=True) 
    cdperiod = models.DateField(blank=False, null=False) 
    product = models.ForeignKey(Tbproduct, on_delete=models.CASCADE)

    @property
    def id(self):
        return self.cvid
    
    def __str__(self):
        return f"Favorite {self.id} - Product {self.product.description}"
