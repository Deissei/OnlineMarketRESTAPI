from rest_framework import viewsets, permissions

from apps.categories.serializers import CategorySerializer
from apps.categories.models import Category


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
