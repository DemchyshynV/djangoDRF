from rest_framework.serializers import ModelSerializer

from .models import OfficeModel


class OfficeSerializer(ModelSerializer):
    class Meta:
        model = OfficeModel
        fields = '__all__'
