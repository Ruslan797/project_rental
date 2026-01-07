# from django.core.validators import MinValueValidator, MaxValueValidator
# from rental_connects.models.accounts import Tenant, Landlord
# from rental_connects.models.address import Address
# from django.db import models
# from django.utils.translation import gettext_lazy as _
# from django.conf import settings
#
# class Advertisement(models.Model):
#     PROPERTY_TYPES = [
#         ('apartment', 'Wohnung'),
#         ('house', 'Haus'),
#         ('room', 'Zimmer'),
#     ]
#
#     STATUS_CHOICES = [
#         ('active', 'Aktiv'),
#         ('archived', 'Archiviert'),
#         ('pending', 'In Prüfung'),
#     ]
#
#     title = models.CharField(max_length=200)
#     type_of_property = models.CharField(max_length=20, choices=PROPERTY_TYPES)
#     description = models.TextField(blank=True)
#     price = models.PositiveIntegerField()
#     area = models.FloatField()
#     number_of_rooms = models.PositiveIntegerField()
#     number_of_floors = models.PositiveIntegerField()
#     address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='advertisement')
#     infrastructure = models.CharField(max_length=200, null=True, blank=True)
#     tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True, blank=True, related_name='advertisements')
#     landlord = models.ForeignKey(Landlord, on_delete=models.SET_NULL, null=True, blank=True, related_name='advertisements')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     deleted_at = models.DateTimeField(null=True, blank=True)
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
#     rating = models.FloatField(
#         validators=[MinValueValidator(0), MaxValueValidator(10)],
#         null=True, blank=True
#     )
#     images = models.ImageField(upload_to='advertisements/', null=True, blank=True)
#
#     def __str__(self):
#         return self.title
#
# class Comment(models.Model):
#     advertisement = models.ForeignKey(
#         "Advertisement",
#         on_delete=models.CASCADE,
#         related_name="comments",
#         verbose_name=_("Advertisement")
#     )
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         on_delete=models.CASCADE,
#         related_name="comments",
#         verbose_name=_("User")
#     )
#     text = models.TextField(verbose_name=_("Comment text"))
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
#     updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))
#
#     def __str__(self):
#         return f"Comment by {self.user.nick_name or self.user.username} on {self.advertisement.title}"
#
#     class Meta:
#         ordering = ["-created_at"]
#         verbose_name = _("Comment")
#         verbose_name_plural = _("Comments")
#
# class RentRequest(models.Model):
#     STATUS_CHOICES = [
#         ('pending', _('In Bearbeitung')),
#         ('approved', _('Bestätigt')),
#         ('rejected', _('Abgelehnt'))
#     ]
#
#     tenant = models.ForeignKey(
#         Tenant,
#         on_delete=models.CASCADE,
#         related_name='rent_requests',
#         verbose_name=_('Mieter')
#     )
#     advertisement = models.ForeignKey(
#         Advertisement,
#         on_delete=models.CASCADE,
#         related_name='rent_requests',
#         verbose_name=_('Anzeige')
#     )
#     status = models.CharField(
#         max_length=10,
#         choices=STATUS_CHOICES,
#         default='pending',
#         verbose_name=_('Status')
#     )
#     created_at = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name=_('Erstellt am')
#     )
#
#     class Meta:
#         verbose_name = _('Mietanfrage')
#         verbose_name_plural = _('Mietanfragen')
#
#     def __str__(self):
#         return f"{self.get_status_display()} - Mietanfrage von {self.tenant.user.email} für {self.advertisement.title}"
#
#
# User = settings.AUTH_USER_MODEL
#
# class Booking(models.Model):
#     tenant = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="bookings"
#     )
#     advertisement = models.ForeignKey(
#         "Advertisement",
#         on_delete=models.CASCADE,
#         related_name="bookings"
#     )
#     start_date = models.DateField()
#     end_date = models.DateField()
#
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         ordering = ["-created_at"]
#
#     def __str__(self):
#         return f"{self.tenant} → {self.advertisement} ({self.start_date} - {self.end_date})"


from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from rental_connects.models.accounts import Tenant, Landlord
from rental_connects.models.address import Address
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings


class Advertisement(models.Model):
    PROPERTY_TYPES = [
        ('apartment', 'Wohnung'),
        ('house', 'Haus'),
        ('room', 'Zimmer'),
    ]

    STATUS_CHOICES = [
        ('active', 'Aktiv'),
        ('archived', 'Archiviert'),
        ('pending', 'In Prüfung'),
    ]

    title = models.CharField(max_length=200)
    type_of_property = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    area = models.FloatField()
    number_of_rooms = models.PositiveIntegerField()
    number_of_floors = models.PositiveIntegerField()
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='advertisement')
    infrastructure = models.CharField(max_length=200, null=True, blank=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.SET_NULL, null=True, blank=True, related_name='advertisements')
    landlord = models.ForeignKey(Landlord, on_delete=models.SET_NULL, null=True, blank=True, related_name='advertisements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    rating = models.FloatField(
        validators=[MinValueValidator(0), MaxValueValidator(10)],
        null=True, blank=True
    )
    images = models.ImageField(upload_to='advertisements/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    advertisement = models.ForeignKey(
        "Advertisement",
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Advertisement")
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("User")
    )
    text = models.TextField(verbose_name=_("Comment text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated at"))

    def __str__(self):
        return f"Comment by {getattr(self.user, 'nick_name', None) or getattr(self.user, 'username', None)} on {self.advertisement.title}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class RentRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', _('In Bearbeitung')),
        ('approved', _('Bestätigt')),
        ('rejected', _('Abgelehnt'))
    ]

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE,
        related_name='rent_requests',
        verbose_name=_('Mieter')
    )
    advertisement = models.ForeignKey(
        Advertisement,
        on_delete=models.CASCADE,
        related_name='rent_requests',
        verbose_name=_('Anzeige')
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name=_('Status')
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Erstellt am')
    )

    class Meta:
        verbose_name = _('Mietanfrage')
        verbose_name_plural = _('Mietanfragen')

    def __str__(self):
        return f"{self.get_status_display()} - Mietanfrage von {self.tenant.user.email} für {self.advertisement.title}"


User = settings.AUTH_USER_MODEL


class Booking(models.Model):
    tenant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    advertisement = models.ForeignKey(
        "Advertisement",
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def clean(self):
        # базовая проверка
        if self.start_date >= self.end_date:
            raise ValidationError({"end_date": "end_date must be after start_date"})

        # overlap: existing.start < new.end AND existing.end > new.start
        qs = Booking.objects.filter(
            advertisement=self.advertisement,
            start_date__lt=self.end_date,
            end_date__gt=self.start_date,
        )
        if self.pk:
            qs = qs.exclude(pk=self.pk)

        if qs.exists():
            raise ValidationError({"detail": "Apartment already booked for selected dates"})

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.tenant} → {self.advertisement} ({self.start_date} - {self.end_date})"

