from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class Tbusertype(models.Model):

    cvid = models.AutoField(primary_key=True)
    ccdescription = models.CharField(max_length=45, blank=False, null=False, unique=True)

    def __str__(self):
        return self.ccdescription or "No description"


class Tbuser(models.Model):

    cvid = models.AutoField(primary_key=True)
    ccname = models.CharField(max_length=45, blank=False, null=False)
    ccemail = models.EmailField(max_length=100, unique=True, blank=False, null=False)
    ccpassword = models.CharField(max_length=256, blank=False, null=False)
    cvusertype = models.ForeignKey(Tbusertype, on_delete=models.CASCADE, related_name="users")

    def __str__(self):
        return self.ccname or "No name"
    @property
    def id(self):
        return self.cvid
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_admin(self):
        return self.cvusertype == Tbusertype.objects.get(ccdescription='admin')
    

    
    
