from django.db import models

from office.models import OfficeModel


class EmployeeModel(models.Model):
    class Meta:
        db_table = 'employees'

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    office = models.ForeignKey(OfficeModel, on_delete=models.CASCADE, related_name='employees')
