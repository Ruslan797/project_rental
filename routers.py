# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
#
# @api_view(["GET"])
# def api_root(request):
#     return Response({
#         "accounts": {
#             "register": "/api/accounts/register/",
#             "login": "/api/accounts/login/",
#             "profile": "/api/accounts/profile/",
#             "dashboard": "/api/accounts/dashboard/"
#         },
#         "rental": {
#             "listings": "/api/rental/listings/",
#             "bookings": "/api/rental/bookings/",
#             "reviews": "/api/rental/reviews/"
#         }
#     })

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
#
#
# @api_view(["GET"])
# def api_root(request):
#     return Response({
#         "accounts": {
#             "register": "/api/accounts/register/",
#             "login": "/api/accounts/login/",
#             "profile": "/api/accounts/profile/",
#             "dashboard": "/api/accounts/dashboard/"
#         },
#         "rental": {
#             "advertisements": "/api/rental/advertisements/",
#             "comments": "/api/rental/comments/"
#         }
#     })
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from rental_connects.views.address import AddressViewSet

router = DefaultRouter()
router.register(r'address', AddressViewSet, basename='address')

# @api_view(["GET"])
# def api_root(request):
#     return Response({
#         "accounts": {
#             "register": "/api/accounts/register/",
#             "login": "/api/accounts/login/",
#             "profile": "/api/accounts/profile/",
#             "dashboard": "/api/accounts/dashboard/"
#         },
#         "rental": {
#             "advertisements": "/api/rental/advertisements/",
#             "comments": "/api/rental/comments/"
#         },
#         "address": "/api/address/"
#     })
@api_view(['GET'])
def api_root(request):
    return Response({
        "accounts": {
            "register": "/api/accounts/register/",
            "login": "/api/accounts/login/",
            "profile": "/api/accounts/profile/",
            "dashboard": "/api/accounts/dashboard/"
        },
        "rental": {
            "advertisements": '/api/rental/advertisements/',
            "comments": '/api/rental/comments/',
            "create_rent_request": '/api/rental/advertisement/<int:advertisement_id>/create_rent_request/'
        },
        "address": "/api/address/"
    })
