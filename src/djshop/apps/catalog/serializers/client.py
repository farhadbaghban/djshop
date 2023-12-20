from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from djshop.apps.catalog.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"