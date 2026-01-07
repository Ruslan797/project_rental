from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    country = models.CharField(max_length=100, verbose_name=_("Country"))
    city = models.CharField(max_length=100, verbose_name=_("City"))
    region = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=255, verbose_name=_("Street"))
    house = models.CharField(max_length=6, verbose_name=_("House Number"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street} {self.house}"

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
