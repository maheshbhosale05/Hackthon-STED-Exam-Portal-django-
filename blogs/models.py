from django.db import models
# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)

class registration(models.Model):
    fname = models.CharField(max_length=80)
    lname = models.CharField(max_length=80)
    father = models.CharField(max_length=80)
    mother = models.CharField(max_length=80)
    bdate = models.CharField(max_length=80)
    mobile = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    sadd = models.CharField(max_length=80)
    padd = models.CharField(max_length=80)
    district = models.CharField(max_length=80)
    state = models.CharField(max_length=80)
    lang = models.CharField(max_length=80)
    cast = models.CharField(max_length=80)
    Category = models.CharField(max_length=80)
    sboard = models.CharField(max_length=80)
    spassyear = models.CharField(max_length=80)
    sscmark = models.CharField(max_length=80)
    sscmarkobt = models.CharField(max_length=80)
    spercentage = models.CharField(max_length=80)
    hboard = models.CharField(max_length=80)
    hpassyear = models.CharField(max_length=80)
    hscmark = models.CharField(max_length=80)
    hscmarkobt = models.CharField(max_length=80)
    hpercentage = models.CharField(max_length=80)
    gboard = models.CharField(max_length=80)
    gpassyear = models.CharField(max_length=80)
    gmark = models.CharField(max_length=80)
    gmarkobt = models.CharField(max_length=80)
    gpercentage = models.CharField(max_length=80)
    ortho = models.CharField(max_length=80)
    previousapp = models.CharField(max_length=80)


class AdminUsers(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)