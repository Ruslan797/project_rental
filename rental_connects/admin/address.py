from django.contrib import admin
from rental_connects.models.address import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ("id", "street", "city", "country")
    search_fields = ("street", "city")
    list_filter = ("city", "country")
    ordering = ("id",)