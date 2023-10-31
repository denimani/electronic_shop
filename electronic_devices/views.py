from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from electronic_devices.models import Supplier, Product, NetworkNode
from electronic_devices.permissions import IsActiveUser
from electronic_devices.serializers import SupplierSerializer, ProductSerializer, NetworkNodeSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsActiveUser, permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser, permissions.IsAuthenticated]


class NetworkNodeViewSet(viewsets.ModelViewSet):
    queryset = NetworkNode.objects.all()
    serializer_class = NetworkNodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']
    permission_classes = [IsActiveUser, permissions.IsAuthenticated]
