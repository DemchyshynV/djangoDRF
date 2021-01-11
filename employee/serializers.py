from rest_framework.serializers import ModelSerializer

from .models import EmployeeModel


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'
        # exclude = ('office',)
        extra_kwargs = {'office': {'read_only': True}}
