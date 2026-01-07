from django.contrib import admin
from rental_connects.models.review import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "advertisement", "user", "rating", "created_at")
    search_fields = ("user__email", "advertisement__title", "text")
    list_filter = ("rating", "created_at")