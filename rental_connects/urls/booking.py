# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from rental_connects.views.booking import (
#     CreateBookingView, MyBookingsView, AdvertisementBusyDatesView
# )
#
# router = DefaultRouter()
# router.register(r"advertisements", AdvertisementViewSet, basename="advertisement")
# router.register(r"comments", CommentViewSet, basename="comment")
#
# urlpatterns = [
#     path("bookings/create/", CreateBookingView.as_view(), name="create-booking"),
#     path("bookings/my/", MyBookingsView.as_view(), name="my-bookings"),
#     path("advertisements/<int:advertisement_id>/busy-dates/", AdvertisementBusyDatesView.as_view(), name="busy-dates"),
#     path("", include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rental_connects.views.booking import (
    AdvertisementViewSet,
    CommentViewSet,
    create_rent_request,
    CreateBookingView,
    MyBookingsView,
    AdvertisementBusyDatesView,
)

router = DefaultRouter()
router.register(r'advertisements', AdvertisementViewSet, basename='advertisement')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    # booking
    path("bookings/create/", CreateBookingView.as_view(), name="create-booking"),
    path("bookings/my/", MyBookingsView.as_view(), name="my-bookings"),
    path("advertisements/<int:advertisement_id>/busy-dates/", AdvertisementBusyDatesView.as_view(), name="busy-dates"),

    # rent request
    path("advertisement/<int:advertisement_id>/create_rent_request/", create_rent_request, name="create_rent_request"),

    # router endpoints
    path("", include(router.urls)),
]

