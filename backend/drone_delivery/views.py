from rest_framework import viewsets, mixins
from drone_delivery.models import DeliveryRun, Location
from drone_delivery.serializers import (
    DeliveryRunListSerializer, 
    DeliveryRunDetailSerializer,
    LocationSerializer
)

class DeliveryRunViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DeliveryRun.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return DeliveryRunListSerializer
        return DeliveryRunDetailSerializer

class LocationViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def health_check(request):
    """
    Simple health check endpoint for Docker orchestration.
    """
    return Response({"status": "healthy", "service": "backend"})

