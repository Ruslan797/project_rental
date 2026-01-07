from rest_framework import viewsets
from rental_connects.models.payments import Payment
from rental_connects.serializers.payments import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
