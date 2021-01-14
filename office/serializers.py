from rest_framework.serializers import ModelSerializer, ValidationError

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

    # def validate(self, attrs):
    #     if attrs.get('city') != attrs.get('name'):
    #         raise ValidationError("citi is not name")
    #     return attrs
    def validate_name(self, name: str):
        if not name.startswith('M'):
            raise ValidationError('name must be start with "M"')
        return name
