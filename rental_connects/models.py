from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Telefonnummer")
    is_landlord = models.BooleanField(default=False, verbose_name="Ist Vermieter")
    is_tenant = models.BooleanField(default=False, verbose_name="Ist Mieter")
    address = models.OneToOneField(to='Address', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Addresse")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email or self.username