from rest_framework import viewsets
from djshop.apps.catalog.serializers.client import CategorySerializer
from djshop.apps.catalog.models import Category


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.public()
    serializer_class = CategorySerializer
