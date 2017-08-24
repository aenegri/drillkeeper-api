from rest_framework import serializers
from .models import Show, Set

class ShowSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Show
        fields = (
            'id',
            'name',
            'date_created',
            'date_modified',
            'author'
            )
        read_only_fields = (
            'date_created',
            'date_modified',
            'author',
             )

class SetSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Set
        fields = (
            'number',
            'subset',
            'counts',
            'yard_line',
            'side',
            'x',
            'hash_line',
            'y',
            'show',
            'author',
            )
        read_only_fields = (
            'author',
        )