from rest_framework import serializers
from electronic_devices.models import Supplier, Product, NetworkNode


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class NetworkNodeSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    supplier = SupplierSerializer()

    class Meta:
        model = NetworkNode
        fields = '__all__'
