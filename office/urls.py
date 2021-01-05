from django.urls import path
from .views import OfficeRetrieveView, OfficeListCreateView, OfficeEmployeeCreateView

urlpatterns = [
    path('', OfficeListCreateView.as_view(), name="office_list_create"),
    path('/<int:id>', OfficeRetrieveView.as_view(), name="office_retrieve"),
    path('/<int:pk>/employees', OfficeEmployeeCreateView.as_view(), name="office_employee_create")

]
