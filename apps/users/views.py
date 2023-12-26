from rest_framework import viewsets, permissions

from django.contrib.auth import get_user_model

from apps.users.serializers import UserCreateSerializer, UserSerializer
from utils.permissions import IsOwner

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return [IsOwner()]
        return [permissions.AllowAny()]
