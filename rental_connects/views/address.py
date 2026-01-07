from rest_framework.viewsets import ModelViewSet
from rental_connects.models.address import Address
from rental_connects.serializers.address import AddressSerializer

class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer