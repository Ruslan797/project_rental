# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#
# class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
#     username_field = "email"

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
#
# class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
#     username_field = 'email'
#
#     def validate(self, attrs):
#         data = super().validate(attrs)
#         return data
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD
