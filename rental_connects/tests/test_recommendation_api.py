from django.urls import reverse
from rest_framework.test import APITestCase

from rental_connects.models.address import Address
from rental_connects.models.booking import Advertisement


class AdvertisementSimilarApiTests(APITestCase):
    def setUp(self):
        self.address1 = Address.objects.create(
            country="Germany",
            city="Hamburg",
            region="Altona",
            postal_code="22765",
            street="Street One",
            house="1"
        )
        self.address2 = Address.objects.create(
            country="Germany",
            city="Hamburg",
            region="Altona",
            postal_code="22767",
            street="Street Two",
            house="2"
        )
        self.address3 = Address.objects.create(
            country="Germany",
            city="Berlin",
            region="Mitte",
            postal_code="10115",
            street="Street Three",
            house="3"
        )

        self.ad1 = Advertisement.objects.create(
            title="Modern apartment in Hamburg",
            type_of_property="apartment",
            description="Beautiful apartment near metro and supermarket",
            price=1200,
            area=55.0,
            number_of_rooms=2,
            number_of_floors=4,
            address=self.address1,
            infrastructure="metro supermarket",
            status="active"
        )
        self.ad2 = Advertisement.objects.create(
            title="Cozy flat in Hamburg",
            type_of_property="apartment",
            description="Nice apartment close to metro and shops",
            price=1250,
            area=54.0,
            number_of_rooms=2,
            number_of_floors=4,
            address=self.address2,
            infrastructure="metro shops",
            status="active"
        )
        self.ad3 = Advertisement.objects.create(
            title="House in Berlin",
            type_of_property="house",
            description="Large family house with garden",
            price=2400,
            area=130.0,
            number_of_rooms=5,
            number_of_floors=2,
            address=self.address3,
            infrastructure="garden parking",
            status="active"
        )

    def test_similar_advertisements_returns_200(self):
        url = f"/api/rental/advertisements/{self.ad1.id}/similar/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_similar_advertisements_does_not_return_same_object(self):
        url = f"/api/rental/advertisements/{self.ad1.id}/similar/"
        response = self.client.get(url)

        returned_ids = [item["id"] for item in response.data]
        self.assertNotIn(self.ad1.id, returned_ids)

    def test_similar_advertisements_contains_similarity_score(self):
        url = f"/api/rental/advertisements/{self.ad1.id}/similar/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        if response.data:
            self.assertIn("similarity_score", response.data[0])