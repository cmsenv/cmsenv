from django.db import models


class User(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    contactno = models.IntegerField()
	
	
class Admin(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)