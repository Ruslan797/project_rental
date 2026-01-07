from rest_framework import serializers
from rental_connects.models.payments import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
