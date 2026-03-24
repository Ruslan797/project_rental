from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from rental_connects.models.accounts import Landlord
from rental_connects.models.address import Address
from rental_connects.models.booking import Advertisement, Comment


User = get_user_model()


class CommentsApiTests(APITestCase):
    def setUp(self):
        self.login_url = "/api/accounts/login/"
        self.comments_url = "/api/rental/comments/"

        self.user = User.objects.create_user(
            email="comment_user@example.com",
            password="StrongPass123!",
            first_name="Anna",
            last_name="Meyer"
        )

        landlord_user = User.objects.create_user(
            email="landlord_comment@example.com",
            password="StrongPass123!",
            first_name="Paul",
            last_name="Becker"
        )
        landlord = Landlord.objects.create(user=landlord_user)

        address = Address.objects.create(
            country="Germany",
            city="Hamburg",
            region="Mitte",
            street="Lange Reihe",
            house="22"
        )

        self.advertisement = Advertisement.objects.create(
            title="Comment Test Apartment",
            type_of_property="apartment",
            description="Good place",
            price=1000,
            area=48.0,
            number_of_rooms=2,
            number_of_floors=2,
            address=address,
            landlord=landlord,
            infrastructure="Bus, shops"
        )

    def authenticate(self):
        response = self.client.post(
            self.login_url,
            {"email": "comment_user@example.com", "password": "StrongPass123!"},
            format="json"
        )
        token = response.data.get("access") or response.data.get("token")
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_authenticated_user_can_create_comment(self):
        self.authenticate()

        data = {
            "advertisement": self.advertisement.id,
            "text": "Very good apartment."
        }

        response = self.client.post(self.comments_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.count(), 1)

    def test_unauthenticated_user_cannot_create_comment(self):
        data = {
            "advertisement": self.advertisement.id,
            "text": "Unauthorized comment"
        }

        response = self.client.post(self.comments_url, data, format="json")
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])