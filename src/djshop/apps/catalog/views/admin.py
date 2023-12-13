from rest_framework import viewsets
from djshop.apps.catalog.serializers.admin import CategorySerializer
from djshop.apps.catalog.models import Category

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer