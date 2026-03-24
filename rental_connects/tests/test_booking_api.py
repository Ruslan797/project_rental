from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from rental_connects.models.accounts import Landlord
from rental_connects.models.address import Address
from rental_connects.models.booking import Advertisement, Booking


User = get_user_model()


class BookingApiTests(APITestCase):
    def setUp(self):
        self.login_url = "/api/accounts/login/"
        self.create_ad_url = "/api/rental/advertisements/"
        self.create_booking_url = "/api/rental/bookings/create/"
        self.my_bookings_url = "/api/rental/bookings/my/"

        self.landlord_user = User.objects.create_user(
            email="landlord_test@example.com",
            password="StrongPass123!",
            first_name="Otto",
            last_name="Schmidt"
        )
        self.landlord = Landlord.objects.create(user=self.landlord_user)

        self.tenant_user = User.objects.create_user(
            email="tenant_test@example.com",
            password="StrongPass123!",
            first_name="Lena",
            last_name="Fischer"
        )

        self.address = Address.objects.create(
            country="Germany",
            city="Hamburg",
            region="Altona",
            street="Ottenser Hauptstraße",
            house="15"
        )

        self.advertisement = Advertisement.objects.create(
            title="Test Apartment",
            type_of_property="apartment",
            description="Nice apartment",
            price=1200,
            area=55.0,
            number_of_rooms=2,
            number_of_floors=3,
            address=self.address,
            landlord=self.landlord,
            infrastructure="Metro, shops"
        )

    def authenticate(self, email, password):
        response = self.client.post(
            self.login_url,
            {"email": email, "password": password},
            format="json"
        )
        token = response.data.get("access") or response.data.get("token")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_landlord_can_create_advertisement(self):
        self.authenticate("landlord_test@example.com", "StrongPass123!")

        data = {
            "title": "New Apartment",
            "type_of_property": "apartment",
            "description": "Bright and clean apartment",
            "price": 1400,
            "area": 60.0,
            "number_of_rooms": 3,
            "number_of_floors": 4,
            "infrastructure": "S-Bahn, supermarket",
            "address": {
                "country": "Germany",
                "city": "Hamburg",
                "region": "Mitte",
                "street": "Bundestraße",
                "house": "7"
            }
        }

        response = self.client.post(self.create_ad_url, data, format="json")
        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_200_OK])

    def test_tenant_can_create_booking(self):
        self.authenticate("tenant_test@example.com", "StrongPass123!")

        data = {
            "advertisement": self.advertisement.id,
            "start_date": "2026-02-10",
            "end_date": "2026-02-15"
        }

        response = self.client.post(self.create_booking_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Booking.objects.filter(advertisement=self.advertisement).exists())

    def test_booking_overlap_is_rejected(self):
        Booking.objects.create(
            tenant=self.tenant_user,
            advertisement=self.advertisement,
            start_date="2026-02-10",
            end_date="2026-02-15"
        )

        self.authenticate("tenant_test@example.com", "StrongPass123!")

        data = {
            "advertisement": self.advertisement.id,
            "start_date": "2026-02-12",
            "end_date": "2026-02-18"
        }

        response = self.client.post(self.create_booking_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)