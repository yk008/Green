from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(default=18)
    gender = models.CharField(max_length=8)
    salary = models.FloatField(default=10000)


class User(models.Model):
    u_name = models.CharField(max_length=32)
    u_password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'

