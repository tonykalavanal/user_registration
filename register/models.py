from django.db import models


class UserDetails(models.Model):
    userid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=75)
    phone = models.BigIntegerField()
    college = models.CharField(max_length=100)
    
