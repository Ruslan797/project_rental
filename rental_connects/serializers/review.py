from rest_framework import serializers
from rental_connects.models.review import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'advertisement', 'user', 'rating', 'comment', 'created_at']
        read_only_fields = ['id', 'created_at']