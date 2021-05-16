from datetime import datetime
from django.db import models
from datetime import datetime

# Create your models here.

# user joins us
class joinUsModel(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=12)
    wpPhone = models.CharField(max_length=12)
    address = models.CharField(max_length=250)
    occupation = models.CharField(max_length=100)
    message = models.CharField(max_length=500,default="")
    date = models.DateTimeField(default=datetime.now,blank=True)
    varified = models.BooleanField(default=False)

    def __str__(self):
        return self.email

# someone fills up help form "how can we help you?"
class helpModel(models.Model):
    help_type = models.CharField(max_length=50,default="Not spacified")
    name = models.CharField(max_length=80)
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=12)
    wpPhone = models.CharField(max_length=12, default="Not available")
    currentAddress = models.CharField(max_length=250)
    permanentAddress = models.CharField(max_length=100,default="Not Available")
    message = models.CharField(max_length=1000,default="Description Not Available")
    date = models.DateTimeField(default=datetime.now,blank=True)
    isHelpReached = models.BooleanField(default=False)
    city = models.CharField(max_length=100,default="")

    def __str__(self):
        return self.name

# contact/query/suggestion form 
class Contact(models.Model):
    suggestion = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=200)

    def __str__(self):
        return self.name