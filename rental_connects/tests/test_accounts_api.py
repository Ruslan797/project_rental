from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class AccountsApiTests(APITestCase):
    def setUp(self):
        self.register_url = "/api/accounts/register/"
        self.login_url = "/api/accounts/login/"
        self.dashboard_url = "/api/accounts/dashboard/"
        self.become_landlord_url = "/api/accounts/become_landlord/"

        self.user_data = {
            "email": "test_user@example.com",
            "password": "StrongPass123!",
            "first_name": "Max",
            "last_name": "Mustermann"
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data, format="json")

        self.assertIn(response.status_code, [status.HTTP_201_CREATED, status.HTTP_200_OK])
        self.assertTrue(User.objects.filter(email=self.user_data["email"]).exists())

    def test_login_user(self):
        User.objects.create_user(
            email=self.user_data["email"],
            password=self.user_data["password"],
            first_name=self.user_data["first_name"],
            last_name=self.user_data["last_name"]
        )

        response = self.client.post(
            self.login_url,
            {
                "email": self.user_data["email"],
                "password": self.user_data["password"]
            },
            format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data or "token" in response.data)

    def test_dashboard_requires_auth(self):
        response = self.client.get(self.dashboard_url)
        self.assertIn(response.status_code, [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN])