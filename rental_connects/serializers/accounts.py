# from rest_framework import serializers
# from rental_connects.models.rental_connects import Address, Landlord, Tenant
#
#
# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = ['id', 'country', 'city', 'street', 'house', 'created_at', 'updated_at']
#         read_only_fields = ['id', 'created_at', 'updated_at']
#
#
# class LandlordSerializer(serializers.ModelSerializer):
#     address = AddressSerializer(read_only=True)
#
#     class Meta:
#         model = Landlord
#         fields = [
#             'id', 'first_name', 'last_name', 'email', 'phone_number',
#             'address', 'date_joined', 'deleted', 'deleted_at'
#         ]
#         read_only_fields = ['id', 'date_joined', 'deleted_at']
#
#
# class TenantSerializer(serializers.ModelSerializer):
#     address = AddressSerializer(read_only=True)  # Вложенный сериализатор для адреса
#
#     class Meta:
#         model = Tenant
#         fields = [
#             'id', 'first_name', 'last_name', 'email', 'phone_number',
#             'address', 'date_joined', 'updated_at', 'deleted', 'deleted_at'
#         ]
#         read_only_fields = ['id', 'date_joined', 'updated_at', 'deleted_at']

# from rest_framework import serializers
# from rest_framework.validators import UniqueValidator
# from django.contrib.auth import get_user_model
# from rental_connects.models.accounts import Landlord, Tenant
# from rental_connects.serializers.address import AddressSerializer
#
# User = get_user_model()
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'first_name', 'last_name', 'date_joined']
#         read_only_fields = ['id', 'date_joined']
#
#
# class LandlordSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     address = AddressSerializer(read_only=True)
#
#     class Meta:
#         model = Landlord
#         fields = [
#             'id', 'user', 'address', 'date_joined',
#             'deleted', 'deleted_at', 'rating'
#         ]
#         read_only_fields = ['id', 'date_joined', 'deleted_at']
#
#
# class TenantSerializer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)
#     address = AddressSerializer(read_only=True)
#
#     class Meta:
#         model = Tenant
#         fields = [
#             'id', 'user', 'address', 'date_joined', 'updated_at',
#             'deleted', 'deleted_at', 'rating'
#         ]
#         read_only_fields = ['id', 'date_joined', 'updated_at', 'deleted_at']
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     nick_name = serializers.CharField(required=False, allow_blank=True, allow_null=True)
#
#     class Meta:
#         model = User
#         fields = ["email", "nick_name", "first_name", "last_name", "password"]
#         extra_kwargs = {
#             "password": {"write_only": True},
#             "first_name": {"required": False},
#             "last_name": {"required": False},
#         }
#
#     def create(self, validated_data):
#         nick = validated_data.get("nick_name")
#
#         if nick:
#             validated_data["username"] = nick
#         else:
#             validated_data["username"] = validated_data["email"]
#
#         validated_data.pop("nick_name", None)
#
#         user = User.objects.create_user(**validated_data)
#         return user
#
# class LoginSerializer(serializers.Serializer):
#     login = serializers.CharField()
#     password = serializers.CharField()
#
#     def validate(self, attrs):
#         login = attrs.get("login")
#         password = attrs.get("password")
#
#         if not login or not password:
#             raise serializers.ValidationError("Login and password are required")
#
#         return attrs

from rest_framework import serializers
from django.contrib.auth import get_user_model

from rental_connects.models.accounts import Landlord, Tenant
from rental_connects.serializers.address import AddressSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "date_joined"]
        read_only_fields = ["id", "date_joined"]


class LandlordSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Landlord
        fields = [
            "id", "user", "address", "date_joined",
            "deleted", "deleted_at", "rating"
        ]
        read_only_fields = ["id", "date_joined", "deleted_at"]


class TenantSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Tenant
        fields = [
            "id", "user", "address", "date_joined", "updated_at",
            "deleted", "deleted_at", "rating"
        ]
        read_only_fields = ["id", "date_joined", "updated_at", "deleted_at"]


# class RegisterSerializer(serializers.ModelSerializer):
#     nick_name = serializers.CharField(
#         required=False,
#         allow_blank=True,
#         allow_null=True
#     )
#
#     class Meta:
#         model = User
#         fields = ["email", "nick_name", "first_name", "last_name", "password"]
#         extra_kwargs = {
#             "password": {"write_only": True},
#             "first_name": {"required": False},
#             "last_name": {"required": False},
#         }
#
#     def create(self, validated_data):
#         """
#         Создание пользователя:
#         - username = nick_name, если указан
#         - иначе username = email
#         - nick_name удаляется, чтобы не ломать create_user()
#         """
#         nick = validated_data.get("nick_name")
#
#         validated_data["username"] = nick if nick else validated_data["email"]
#
#         validated_data.pop("nick_name", None)
#
#         return User.objects.create_user(**validated_data)

# class RegisterSerializer(serializers.ModelSerializer):
#     nick_name = serializers.CharField(
#         required=False,
#         allow_blank=True,
#         allow_null=True
#     )
#
#     class Meta:
#         model = User
#         fields = ["email", "nick_name", "first_name", "last_name", "password"]
#         extra_kwargs = {
#             "password": {"write_only": True},
#             "first_name": {"required": False},
#             "last_name": {"required": False},
#         }
#
#     def create(self, validated_data):
#         """
#         Создание пользователя:
#         - username НЕ используется (username=None в модели)
#         - nick_name сохраняется как поле модели
#         """
#         validated_data.pop("nick_name", None)  # если хочешь — можешь оставить
#
#         return User.objects.create_user(**validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    nick_name = serializers.CharField(
        required=False,
        allow_blank=True,
        allow_null=True
    )

    class Meta:
        model = User
        fields = ["email", "nick_name", "first_name", "last_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
            "first_name": {"required": False},
            "last_name": {"required": False},
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже существует.")
        return value

    def create(self, validated_data):
        """
        Создание пользователя:
        - username НЕ используется (username=None в модели)
        - nick_name сохраняется как поле модели
        """
        return User.objects.create_user(**validated_data)



class LoginSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        login = attrs.get("login")
        password = attrs.get("password")

        if not login or not password:
            raise serializers.ValidationError("Login and password are required")

        return attrs


