from django.db import models


# Create your models here.

class OfficeModel(models.Model):
    name = models.CharField(max_length=10)
    city = models.CharField(max_length=20)

    class Meta:
        db_table = 'office'

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return f'{self.__dict__}'


class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    city = models.CharField(max_length=30)
    # office = models.OneToOneField(OfficeModel,on_delete=models.CASCADE)
    # offices = models.ForeignKey(OfficeModel, on_delete=models.CASCADE, related_name="employee")
    offices = models.ManyToManyField(OfficeModel, related_name="employees", db_column='office_employee')

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return f'{self.__dict__}'
