from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import mixins
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework_jwt.views import ObtainJSONWebToken

from utils.MyAuth import MyAuth
from utils.MyPermission import MyPermission
from . import serializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

User = get_user_model()


# Create your views here.
class Login(ObtainJSONWebToken):
    permission_classes = [AllowAny]


class RegisterView(CreateAPIView):
    serializer_class = serializer.RegisterSerializer
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = [AllowAny]


class UsernameValidateView(APIView):
    """
    校验用户名
    """

    def get(self, request, username):
        data_dict = {
            "username": username,
            "count": User.objects.filter(username=username).count()
        }
        return Response(data_dict)


class EmailValidateView(APIView):
    """
    校验邮箱
    """

    def get(self, request, email):
        data_dict = {
            "email": email,
            "count": User.objects.filter(email=email).count()
        }
        return Response(data_dict)


class UserView(mixins.UpdateModelMixin,
               mixins.ListModelMixin,
               GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
    lookup_field = "username"
    # filterset_fields = ("username",)
    ordering_fields = "__all__"
    authentication_classes = [MyAuth, ]
    # IsAdminUser 权限仅允许 user.is_staff 为 True 用户访问，其他任何用户都将被拒绝。
    # permission_classes = [IsAdminUser, ]
    permission_classes = [MyPermission, ]

    # search_fields = "__all__"
    # pagination_class = None

    # def list(self, request, *args, **kwargs):
    #     data = super().list(request, *args, **kwargs)
    #     return Response(data)

    def update(self, request, *args, **kwargs):
        request.data["password"] = make_password(request.data["password"])
        return super().update(request, *args, **kwargs)


class AvatarView(mixins.UpdateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
    lookup_field = "username"
    permission_classes = [MyPermission, ]

    # def update(self, request, *args, **kwargs):
    #     file = request.FILES.get('img')
    #     user = self.get_object()
    #     # user = request.user
    #     user.avatar = file
    #     user.save()
    #     pass
