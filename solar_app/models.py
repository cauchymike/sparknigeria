import email
from django.db import models

# Create your models here.


class BusinessInvestor(models.Model):
    firstname =  models.CharField(max_length=45,null=True)
    lastname = models.CharField(max_length=45,null=True)
    emailaddress = models.CharField(max_length=45,null=True,unique=True)
    companyname = models.CharField(max_length=250,default="")
    country = models.CharField(max_length=45,default="",null=True)
    phonenumber = models.CharField(max_length=45,null=True)
    password = models.CharField(max_length=250,default="")

class IndividualInvestor(models.Model):
    firstname =  models.CharField(max_length=45,null=True)
    lastname = models.CharField(max_length=45,null=True)
    emailaddress = models.CharField(max_length=45,null=True,unique=True)
    password = models.CharField(max_length=250,default="")
    about_us = models.CharField(max_length=45,default="")

class Affliates(models.Model):
    fullname = models.CharField(max_length=45,null=True)
    phonenumber = models.CharField(max_length=45,null=True)
    emailaddress = models.CharField(max_length=45,null=True,unique=True)
    address = models.CharField(max_length=250,default="")
    fullname_kin = models.CharField(max_length=45,null=True)
    phonenumber_kin = models.CharField(max_length=45,null=True)
    password = models.CharField(max_length=250,default="")

class Sponsor(models.Model):
    fullname = models.CharField(max_length=45,null=True)
    phonenumber = models.CharField(max_length=45,null=True)
    emailaddress = models.CharField(max_length=45,null=True,unique=True)
    address = models.CharField(max_length=250,default="")
    fullname_kin = models.CharField(max_length=45,null=True)
    phonenumber_kin = models.CharField(max_length=45,null=True)
    password = models.CharField(max_length=250,default="")

class Dashboard(models.Model):
    date_of_sale = models.DateField()
    sale_type = models.CharField(max_length=45,null=True)
    sale_earnings = models.DecimalField(
        default=0, max_digits=16, decimal_places=2)
    earning_duration = models.CharField(max_length=45,null=True)
    affliateID = models.ForeignKey(Affliates,on_delete=models.CASCADE,null=True) 

class Pitch(models.Model):
    firstname = models.CharField(max_length=45,null=True)
    lastname = models.CharField(max_length=45,null=True)
    emailaddress = models.CharField(max_length=45,null=True,unique=True)
    phonenumber = models.CharField(max_length=45,null=True)
    city  = models.CharField(max_length=45,null=True)
    no_of_users = models.DecimalField(
        default=0, max_digits=16, decimal_places=2)
    load_capacity = models.DecimalField(
        default=0, max_digits=16, decimal_places=2)
    extra_details = models.CharField(max_length=500,default="")
    created_at = models.DateTimeField(
        'created_at', auto_now_add=True, null=True)



    


    

