from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from user.serializers import UserSerializer


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
