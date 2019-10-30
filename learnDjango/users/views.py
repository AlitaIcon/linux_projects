from rest_framework.generics import CreateAPIView
from . import serializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# Create your views here.

class RegisterView(CreateAPIView):
    serializer_class = serializer.RegisterSerializer
    authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = [AllowAny]
