import django_filters
from django.db.models import Q
from rental_connects.models.booking import Advertisement


class AdvertisementFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    min_rooms = django_filters.NumberFilter(field_name="number_of_rooms", lookup_expr="gte")
    max_rooms = django_filters.NumberFilter(field_name="number_of_rooms", lookup_expr="lte")

    min_area = django_filters.NumberFilter(field_name="area", lookup_expr="gte")
    max_area = django_filters.NumberFilter(field_name="area", lookup_expr="lte")

    min_floors = django_filters.NumberFilter(field_name="number_of_floors", lookup_expr="gte")
    max_floors = django_filters.NumberFilter(field_name="number_of_floors", lookup_expr="lte")

    country = django_filters.CharFilter(field_name="address__country", lookup_expr="icontains")
    city = django_filters.CharFilter(field_name="address__city", lookup_expr="icontains")
    region = django_filters.CharFilter(field_name="address__region", lookup_expr="icontains")
    street = django_filters.CharFilter(field_name="address__street", lookup_expr="icontains")

    min_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="gte")
    max_rating = django_filters.NumberFilter(field_name="rating", lookup_expr="lte")

    landlord = django_filters.NumberFilter(field_name="landlord__id", lookup_expr="exact")

    created_after = django_filters.DateFilter(field_name="created_at", lookup_expr="gte")
    created_before = django_filters.DateFilter(field_name="created_at", lookup_expr="lte")

    search = django_filters.CharFilter(method="filter_search")

    class Meta:
        model = Advertisement
        fields = ["type_of_property", "status"]

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(title__icontains=value) |
            Q(description__icontains=value) |
            Q(infrastructure__icontains=value)
        )










