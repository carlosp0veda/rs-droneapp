from rest_framework import serializers
from django.contrib.gis.geos import Point
from drone_delivery.models import Operator, DeliveryRun, Location, Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer_name', 'items', 'instructions']

class LocationSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)
    coordinates = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = [
            'id', 'sequence_order', 'category', 'name', 
            'coordinates', 'status', 'order'
        ]

    def get_coordinates(self, obj):
        return {
            'latitude': obj.coordinates.y,
            'longitude': obj.coordinates.x
        }

class DeliveryRunListSerializer(serializers.ModelSerializer):
    total_locations = serializers.SerializerMethodField()

    class Meta:
        model = DeliveryRun
        fields = ['id', 'status', 'started_at', 'total_locations']

    def get_total_locations(self, obj):
        return obj.locations.count()

class DeliveryRunDetailSerializer(serializers.ModelSerializer):
    locations = LocationSerializer(many=True, read_only=True)

    class Meta:
        model = DeliveryRun
        fields = ['id', 'status', 'started_at', 'completed_at', 'metadata', 'locations']
