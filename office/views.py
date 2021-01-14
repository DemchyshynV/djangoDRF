from django.db.models import Prefetch, F
from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import OfficeSerializer
from .models import OfficeModel
from employee.serializers import EmployeeSerializer
from employee.models import EmployeeModel
from user.permissions import IsSuperUser


class OfficeListCreateView(ListCreateAPIView):
    authentication_classes = []
    # permission_classes = (IsSuperUser,)
    serializer_class = OfficeSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city')
        age = self.request.query_params.getlist('age')
        qs = OfficeModel.objects.all()
        if city:
            qs = qs.filter(city__iexact=city)
        if age and len(age) == 2:
            objects_filter = EmployeeModel.objects.filter(age__range=age, city__iexact=F('office__city'))
            qs = qs.prefetch_related(Prefetch('employees', objects_filter))
        return qs


class OfficeRetrieveView(DestroyAPIView, UpdateModelMixin):
    queryset = OfficeModel.objects
    serializer_class = OfficeSerializer
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class OfficeEmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        office_id = self.kwargs.get('pk')
        office = get_object_or_404(OfficeModel, pk=office_id)
        serializer.save(office=office)
