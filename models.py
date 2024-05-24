from django.db import models

# Create your models here.
class recruitment(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=13)
    email=models.CharField(max_length=50)
    