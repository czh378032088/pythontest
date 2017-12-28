from django.db import models

# Create your models here.

class TestTable(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    date = models.DateField(auto_now = True)
