# from rest_framework import viewsets, filters
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from django_filters.rest_framework import DjangoFilterBackend
#
# from rental_connects.models.review import Review
# from rental_connects.serializers.review import ReviewSerializer
#
#
# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     # Фильтрация, поиск, сортировка
#     filter_backends = [
#         DjangoFilterBackend,
#         filters.SearchFilter,
#         filters.OrderingFilter,
#     ]
#
#     # Фильтры по рейтингу, объявлению, пользователю
#     filterset_fields = {
#         "rating": ["exact", "gte", "lte"],
#         "advertisement": ["exact"],
#         "user": ["exact"],
#     }
#
#     # Поиск
#     search_fields = ["text", "user__email", "advertisement__title"]
#
#     # Сортировка
#     ordering_fields = ["rating", "created_at"]
#
#     # Автопривязка пользователя
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from rental_connects.models.review import Review
from rental_connects.serializers.review import ReviewSerializer
from rental_connects.pagination import ReviewPagination

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ReviewPagination

    # Фильтрация, поиск, сортировка
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    # Фильтры по рейтингу, объявлению, пользователю
    filterset_fields = {
        "rating": ["exact", "gte", "lte"],
        "advertisement": ["exact"],
        "user": ["exact"],
    }

    # Поиск
    search_fields = ["text", "user__email", "advertisement__title"]

    # Сортировка
    ordering_fields = ["rating", "created_at"]

    # Автопривязка пользователя
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)