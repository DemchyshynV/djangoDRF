from rest_framework.generics import RetrieveAPIView, ListAPIView
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CurrentUserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        return user
