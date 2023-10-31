from rest_framework.routers import DefaultRouter

from electronic_devices.apps import ElectronicDevicesConfig
from electronic_devices.views import SupplierViewSet, ProductViewSet, NetworkNodeViewSet

app_name = ElectronicDevicesConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'network-nodes', NetworkNodeViewSet, basename='network-nodes')

urlpatterns = router.urls
