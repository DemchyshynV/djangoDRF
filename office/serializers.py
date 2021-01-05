from rest_framework.serializers import ModelSerializer

from .models import OfficeModel
from employee.serializers import EmployeeSerializer


class OfficeSerializer(ModelSerializer):
    employees = EmployeeSerializer(many=True)

    class Meta:
        model = OfficeModel
        fields = '__all__'
