from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .user_manager import UserManager



class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    nick_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Phone number"))
    is_landlord = models.BooleanField(default=False, verbose_name=_("Is landlord"))
    is_tenant = models.BooleanField(default=False, verbose_name=_("Is tenant"))
    address = models.OneToOneField("Address", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Address"))

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.nick_name or self.email


class Landlord(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="landlord_profile", null=True, blank=True)
    address = models.OneToOneField("Address", null=True, on_delete=models.SET_NULL, related_name="landlord")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date joined"))
    deleted = models.BooleanField(default=False, verbose_name=_("Deleted"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Deleted at"))
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null=True,
        blank=True,
        verbose_name=_("Rating")
    )

    def __str__(self):
        return f"{self.user.nick_name} {self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ["-date_joined"]
        get_latest_by = "date_joined"
        verbose_name = _("Landlord")
        verbose_name_plural = _("Landlords")


class Tenant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tenant_profile", null=True, blank=True)
    address = models.OneToOneField("Address", null=True, on_delete=models.SET_NULL, related_name="tenant")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name=_("Date joined"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
    deleted = models.BooleanField(default=False, verbose_name=_("Deleted"))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_("Deleted at"))
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null=True,
        blank=True,
        verbose_name=_("Rating")
    )

    def __str__(self):
        return f"{self.user.nick_name} {self.user.first_name} {self.user.last_name}"

    class Meta:
        ordering = ["-date_joined"]
        get_latest_by = "date_joined"
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")



