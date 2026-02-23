from django.http import JsonResponse
from rest_framework import viewsets
from .models import Product, Order, OrderItem
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session['cart'] = cart

    return JsonResponse({"message": "Product added to cart", "cart": cart})

def view_cart(request):
    cart = request.session.get('cart', {})
    return JsonResponse({"cart": cart})
