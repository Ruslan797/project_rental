from rest_framework_simplejwt.views import TokenObtainPairView
from rental_connects.serializers.token import EmailTokenObtainPairSerializer

class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


