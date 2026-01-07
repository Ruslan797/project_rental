# from django.contrib import admin
# from rental_connects.models.booking import Advertisement, Comment, RentRequest
# from rental_connects.models.accounts import Tenant, Landlord
#
#
# @admin.register(Advertisement)
# class AdvertisementAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "title",
#         "type_of_property",
#         "price",
#         "area",
#         "number_of_rooms",
#         "landlord",
#         "tenant",
#         "status",
#         "created_at",
#     )
#
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ("id", "advertisement", "user", "created_at")
#     search_fields = ("user__email", "advertisement__title", "text")
#     list_filter = ("created_at",)
#
#
# @admin.register(RentRequest)
# class RentRequestAdmin(admin.ModelAdmin):
#     list_display = ('id', 'tenant', 'advertisement', 'status', 'created_at')
#     list_filter = ('status', 'created_at')
#     search_fields = ('tenant__user__email', 'advertisement__title')
#     actions = ['approve_requests', 'reject_requests']
#
#     def approve_requests(self, request, queryset):
#         queryset.update(status='approved')
#         for rent_request in queryset:
#             rent_request.advertisement.tenant = rent_request.tenant
#             rent_request.advertisement.status = 'active'
#             rent_request.advertisement.save()
#     approve_requests.short_description = "Approve selected requests"
#
#     def reject_requests(self, request, queryset):
#         queryset.update(status='rejected')
#     reject_requests.short_description = "Reject selected requests"
#
#
# @admin.register(Tenant)
# class TenantAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user_email', 'rating')
#     search_fields = ('user__email',)
#
#     def user_email(self, obj):
#         return obj.user.email
#     user_email.short_description = 'Email'
#
# @admin.register(Landlord)
# class LandlordAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user_email', 'rating')
#     search_fields = ('user__email',)
#
#     def user_email(self, obj):
#         return obj.user.email
#     user_email.short_description = 'Email'


from django.contrib import admin
from rental_connects.models.booking import Advertisement, Comment, RentRequest

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "type_of_property",
        "price",
        "area",
        "number_of_rooms",
        "landlord_email",
        "tenant_email",
        "status",
        "created_at",
    )
    list_filter = ("status", "type_of_property", "created_at")
    search_fields = ("title", "description", "address__city")

    def landlord_email(self, obj):
        return obj.landlord.user.email if obj.landlord else None
    landlord_email.short_description = "Landlord Email"

    def tenant_email(self, obj):
        return obj.tenant.user.email if obj.tenant else None
    tenant_email.short_description = "Tenant Email"

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "advertisement", "user_email", "created_at", "short_text")
    search_fields = ("user__email", "advertisement__title", "text")
    list_filter = ("created_at", "user__is_active", "advertisement__status")
    readonly_fields = ("created_at",)

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "User Email"

    def short_text(self, obj):
        return obj.text[:50] + "..." if len(obj.text) > 50 else obj.text
    short_text.short_description = "Text Preview"

@admin.register(RentRequest)
class RentRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'tenant', 'advertisement', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('tenant__user__email', 'advertisement__title')
    actions = ['approve_requests', 'reject_requests']

    def approve_requests(self, request, queryset):
        queryset.update(status='approved')
        for rent_request in queryset:
            rent_request.advertisement.tenant = rent_request.tenant
            rent_request.advertisement.status = 'active'
            rent_request.advertisement.save()
    approve_requests.short_description = "Approve selected requests"

    def reject_requests(self, request, queryset):
        queryset.update(status='rejected')
    reject_requests.short_description = "Reject selected requests"



