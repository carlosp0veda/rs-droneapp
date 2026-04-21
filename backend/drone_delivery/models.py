import uuid
from django.contrib.gis.db import models
from django.db.models import JSONField

class Operator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    license_number = models.CharField(max_length=50, unique=True)
    certification_level = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.license_number} ({self.certification_level})"

class DeliveryRun(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    STATUS_CHOICES = [
        ('PLANNING', 'Planning'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    ]
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE, related_name='runs')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNING')
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    metadata = JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Run {self.id} - {self.status}"

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    CATEGORY_CHOICES = [
        ('PICKUP', 'Pickup'),
        ('DELIVERY', 'Delivery'),
    ]
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ARRIVED', 'Arrived'),
        ('COMPLETED', 'Completed'),
    ]
    run = models.ForeignKey(DeliveryRun, on_delete=models.CASCADE, related_name='locations')
    sequence_order = models.PositiveIntegerField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    coordinates = models.PointField(srid=4326)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    class Meta:
        ordering = ['sequence_order']

    def __str__(self):
        return f"{self.sequence_order}: {self.name} ({self.category})"

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='order')
    customer_name = models.CharField(max_length=255)
    items = JSONField(default=list)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return f"Order for {self.customer_name}"
