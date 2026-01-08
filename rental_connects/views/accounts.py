from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from rental_connects.models.accounts import Landlord

from rental_connects.models.accounts import User
from rental_connects.serializers.accounts import UserSerializer, RegisterSerializer, LoginSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def register_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        # назначаем роль Tenant по умолчанию
        tenant_group, _ = Group.objects.get_or_create(name="Tenant")
        user.groups.add(tenant_group)
        return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        login = serializer.validated_data["login"]
        password = serializer.validated_data["password"]

        user = authenticate(request, username=login, password=password)

        if user:
            return Response({
                "message": "Login successful",
                "user": UserSerializer(user).data
            })

        return Response(
            {"error": "Incorrect email or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# def become_landlord_view(request):
#     user = request.user
#     landlord_group, created = Group.objects.get_or_create(name="Landlord")
#     user.groups.add(landlord_group)
#     return Response({"message": "Now you are a Landlord"}, status=status.HTTP_200_OK)



@api_view(["POST"])
@permission_classes([IsAuthenticated])
def become_landlord_view(request):
    user = request.user

    landlord_group, _ = Group.objects.get_or_create(name="Landlord")
    user.groups.add(landlord_group)

    landlord, created = Landlord.objects.get_or_create(user=user)

    return Response(
        {
            "message": "Now you are a Landlord",
            "landlord_id": landlord.id,
            "landlord_created": created
        },
        status=status.HTTP_200_OK
    )


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def profile_view(request):
    return Response(UserSerializer(request.user).data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    if request.user.groups.filter(name="Landlord").exists():
        role = "Landlord"
    else:
        role = "Tenant"
    return Response({"role": role})

