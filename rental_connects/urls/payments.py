from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rental_connects.views.payments import PaymentViewSet

router = DefaultRouter()
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
