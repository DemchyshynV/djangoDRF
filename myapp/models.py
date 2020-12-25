from django.db import models


# Create your models here.

class OfficeModel(models.Model):
    name = models.CharField(max_length=10)
    city = models.CharField(max_length=20)

    class Meta:
        db_table = 'office'
