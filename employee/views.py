from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import EmployeeModel
from .serializers import EmployeeSerializer


class EmployeeListView(APIView):

    @staticmethod
    def get(*args, **kwargs):
        qs = EmployeeModel.objects.all()
        data = EmployeeSerializer(qs, many=True).data
        return Response(data, status.HTTP_201_CREATED)
