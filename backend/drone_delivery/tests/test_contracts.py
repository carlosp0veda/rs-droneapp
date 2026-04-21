from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from drone_delivery.models import Operator, DeliveryRun

class ContractTests(APITestCase):
    def setUp(self):
        self.operator = Operator.objects.create(
            license_number="DRN-123",
            certification_level="ADVANCED"
        )
        self.run = DeliveryRun.objects.create(operator=self.operator)
        self.url = reverse('deliveryrun-list')

    def test_get_delivery_runs_list(self):
        """
        Verify GET /api/v1/delivery-runs/ matches the contract in api-v1.md
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Verify JSON structure
        data = response.json()
        self.assertIsInstance(data, list)
        if len(data) > 0:
            item = data[0]
            self.assertIn('id', item)
            self.assertIn('status', item)
            self.assertIn('total_locations', item)
