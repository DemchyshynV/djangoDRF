from django.db.models import Prefetch, F
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import OfficeSerializer
from .models import OfficeModel
from employee.serializers import EmployeeSerializer
from employee.models import EmployeeModel


class OfficeListCreateView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        city = self.request.query_params.get('city')
        age = self.request.query_params.getlist('age')
        qs = OfficeModel.objects.all()
        if city:
            qs = qs.filter(city__iexact=city)
        if age:
            objects_filter = EmployeeModel.objects.filter(age__range=age, city__iexact=F('office__city'))
            qs = qs.prefetch_related(Prefetch('employees', objects_filter))
        serializer = OfficeSerializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OfficeRetrieveView(APIView):
    def delete(self, *args, **kwargs):
        id = kwargs.get('id')
        get_object_or_404(OfficeModel, pk=id).delete()
        return Response("ok", status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        id = kwargs.get('id')
        data = self.request.data
        instance = get_object_or_404(OfficeModel, pk=id)
        serializer = OfficeSerializer(instance=instance, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class OfficeEmployeeCreateView(APIView):
    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        office = get_object_or_404(OfficeModel, pk=pk)
        serializer = EmployeeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.save(office_id=pk)
        serializer.save(office=office)
        return Response(serializer.data)
