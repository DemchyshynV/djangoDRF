from django.urls import path

from .views import UserListCreateView, CurrentUserView, UpUserToAdminView
urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_crate'),
    path('/current', CurrentUserView.as_view(), name='user_current'),
    path('/<int:pk>', UpUserToAdminView.as_view(), name='user_up_to_admin')
]
