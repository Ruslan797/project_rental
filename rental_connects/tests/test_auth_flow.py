from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


User = get_user_model()


class AuthFlowTests(APITestCase):
    def setUp(self):
        self.register_url = "/api/accounts/register/"
        self.login_url = "/api/accounts/login/"
        self.dashboard_url = "/api/accounts/dashboard/"

        self.user_data = {
            "email": "new_test_user_01@example.com",
            "password": "StrongPass123!",
            "first_name": "Max",
            "last_name": "Muster"
        }

    def test_full_auth_flow(self):
        # 1. Register new user
        register_response = self.client.post(
            self.register_url,
            self.user_data,
            format="json"
        )

        self.assertIn(
            register_response.status_code,
            [status.HTTP_201_CREATED, status.HTTP_200_OK]
        )
        self.assertTrue(User.objects.filter(email=self.user_data["email"]).exists())

        # 2. Login
        login_response = self.client.post(
            self.login_url,
            {
                "email": self.user_data["email"],
                "password": self.user_data["password"]
            },
            format="json"
        )

        self.assertEqual(login_response.status_code, status.HTTP_200_OK)

        # 3. Get token from response
        token = login_response.data.get("access") or login_response.data.get("token")
        self.assertIsNotNone(token)

        # 4. Use token for protected endpoint
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

        dashboard_response = self.client.get(self.dashboard_url)

        self.assertEqual(dashboard_response.status_code, status.HTTP_200_OK)