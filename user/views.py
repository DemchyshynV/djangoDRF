from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, UpdateAPIView
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer,UpToAdminSerializer
from .permissions import IsSuperUser


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CurrentUserView(RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        return user


class UpUserToAdminView(UpdateAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsSuperUser,)
    queryset = User.objects.all()
    serializer_class = UpToAdminSerializer

    def put(self, request, *args, **kwargs):
        user: User = self.get_object()
        user.is_staff = True
        user.save()
        return super().put(request, *args, **kwargs)
