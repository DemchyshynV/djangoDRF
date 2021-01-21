from django.urls import path

from .views import UserListView, CurrentUserView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list_crate'),
    path('/current', CurrentUserView.as_view(), name='user_current'),
]
