from django.db import models
from django.db.models import Model


# Create your models here.
class Registration(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Username = models.CharField(max_length=200)
    MobileNumber = models.CharField(max_length=10)
    Email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    class Meta:
        db_table = 'reg_table'