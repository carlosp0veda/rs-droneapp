from django.test import TestCase
from django.contrib.gis.geos import Point
from drone_delivery.models import Operator, DeliveryRun, Location, Order

class ModelTests(TestCase):
    def setUp(self):
        self.operator = Operator.objects.create(
            license_number="DRN-123",
            certification_level="ADVANCED"
        )
        self.run = DeliveryRun.objects.create(operator=self.operator)

    def test_delivery_run_creation(self):
        self.assertEqual(self.run.status, 'PLANNING')
        self.assertEqual(str(self.run), f"Run {self.run.id} - PLANNING")

    def test_location_sequencing(self):
        l1 = Location.objects.create(
            run=self.run,
            sequence_order=1,
            category='PICKUP',
            coordinates=Point(-74.0060, 40.7128),
            name="Joe's Pizza"
        )
        l2 = Location.objects.create(
            run=self.run,
            sequence_order=2,
            category='DELIVERY',
            coordinates=Point(-74.0050, 40.7130),
            name="Alice's Home"
        )
        locations = self.run.locations.all()
        self.assertEqual(locations[0], l1)
        self.assertEqual(locations[1], l2)

    def test_order_associated_with_location(self):
        location = Location.objects.create(
            run=self.run,
            sequence_order=1,
            category='PICKUP',
            coordinates=Point(-74.0060, 40.7128),
            name="Joe's Pizza"
        )
        order = Order.objects.create(
            location=location,
            customer_name="Alice Smith",
            instructions="Wait at side door"
        )
        self.assertEqual(location.order, order)
        self.assertEqual(str(order), "Order for Alice Smith")
