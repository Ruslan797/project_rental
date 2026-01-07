__all__ = [
    "AddressSerializer",
    "UserSerializer",
    "LandlordSerializer",
    "TenantSerializer",
    "RegisterSerializer",
    "LoginSerializer",
    "AdvertisementSerializer",
    "CommentSerializer",
    "PaymentSerializer",
]

from .address import AddressSerializer
from .accounts import (
    UserSerializer,
    LandlordSerializer,
    TenantSerializer,
    RegisterSerializer,
    LoginSerializer,
)
from .booking import AdvertisementSerializer, CommentSerializer
from .payments import PaymentSerializer