from rest_framework import serializers

from apps.categories.models import Category


class ParentForCategorySerializer(serializers.ModelSerializer):
    """ Serializer for Parent For Category """

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent',
        )


class CategorySerializer(serializers.ModelSerializer):
    """ Serializer for Categories """

    parent = ParentForCategorySerializer(read_only=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'parent',
        )
