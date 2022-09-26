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

