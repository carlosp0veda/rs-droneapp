from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.gis.geos import Point
from drone_delivery.models import Operator, DeliveryRun, Location, Order

class ViewTests(APITestCase):
    def setUp(self):
        self.operator = Operator.objects.create(
            license_number="DRN-123",
            certification_level="ADVANCED"
        )
        self.run = DeliveryRun.objects.create(operator=self.operator)
        
        # Create sequenced locations
        self.loc1 = Location.objects.create(
            run=self.run,
            sequence_order=1,
            category='PICKUP',
            coordinates=Point(-74.0060, 40.7128),
            name="Joe's Pizza"
        )
        self.loc2 = Location.objects.create(
            run=self.run,
            sequence_order=2,
            category='DELIVERY',
            coordinates=Point(-74.0050, 40.7130),
            name="Alice's Home"
        )
        Order.objects.create(
            location=self.loc1,
            customer_name="Alice Smith",
            instructions="Wait at side door"
        )

    def test_run_detail_includes_sequenced_locations(self):
        url = reverse('deliveryrun-detail', kwargs={'pk': self.run.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.json()
        self.assertEqual(data['id'], str(self.run.id))
        self.assertEqual(len(data['locations']), 2)
        
        # Verify sequence and data
        loc1_data = data['locations'][0]
        self.assertEqual(loc1_data['name'], "Joe's Pizza")
        self.assertEqual(loc1_data['category'], "PICKUP")
        self.assertEqual(loc1_data['order']['customer_name'], "Alice Smith")
        
        # Verify coordinates format
        self.assertEqual(loc1_data['coordinates']['latitude'], 40.7128)
        self.assertEqual(loc1_data['coordinates']['longitude'], -74.0060)

    def test_run_list_provides_summary(self):
        url = reverse('deliveryrun-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['total_locations'], 2)
