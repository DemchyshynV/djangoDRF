from rest_framework.serializers import ModelSerializer

from .models import OfficeModel
from employee.serializers import EmployeeSerializer


class OfficeSerializer(ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = OfficeModel
        fields = '__all__'
        # extra_kwargs = {
        #     'employees':{'read_only':True}
        # }
