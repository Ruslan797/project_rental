from rest_framework.routers import DefaultRouter
from rental_connects.views.review import ReviewViewSet

router = DefaultRouter()
router.register("", ReviewViewSet)  # пустая строка!

urlpatterns = router.urls