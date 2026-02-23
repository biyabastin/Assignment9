from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, OrderItemViewSet
from .views import add_to_cart, view_cart

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)

urlpatterns = [
    path('cart/add/<int:product_id>/', add_to_cart),
    path('cart/', view_cart),
]

urlpatterns += router.urls
