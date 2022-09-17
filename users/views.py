from users.models import CustomUser

from users.serializers import CreateUserProfileSerializer, CustomTokenRefreshSerializer, MyTokenObtainPairSerializer
from rest_framework import generics, status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class UsersList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserProfileSerializer

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserProfileSerializer

    def get_tokens_for_user(self, serializer):
        user = CustomUser.objects.get(pk=serializer['id'])
        refresh = RefreshToken.for_user(user)

        return {
            'id':user.id,
            'name': user.name,
            'email':user.email,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_tokens_for_user(serializer.data), status=status.HTTP_201_CREATED, headers=headers)
        

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom Refresh token View
    """
    serializer_class = CustomTokenRefreshSerializer