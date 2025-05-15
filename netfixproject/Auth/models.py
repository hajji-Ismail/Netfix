from django.db import models

class Register( models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50 , unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    

