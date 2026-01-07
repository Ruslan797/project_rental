from rest_framework import serializers
from rental_connects.models.address import Address



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["country", "city", "region", "postal_code", "street", "house"]
        extra_kwargs = {
            'region': {'required': False},
            'postal_code': {'required': False}
        }

