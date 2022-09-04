from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Cart, CartItem
from products.models import *
from rest_framework.permissions import IsAuthenticated
from .serializers import *


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        # data = request.data
        cart = Cart.objects.filter(user=user, ordered=False).first()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response({'count': len(serializer.data), 'data': serializer.data})

    def post(self, request):
        data = request.data
        user = request.user
        product = Product.objects.get(id=data.get('product'))

        cart_ob, _ = Cart.objects.get_or_create(user=user, ordered=False)
        print(cart_ob)
        price = product.price
        quantity = data.get('quantity')
        cart_items = CartItem(cart=cart_ob, user=user, price=price, product=product, quantity=quantity)
        cart_items.save()
        return Response({'success': 'Item added to cart'})

    def put(self,request):
        data = request.data
        user = request.user
        cart_items = CartItem.objects.get(id=data.get('id'))
        cart_items.quantity += data.get("quantity")
        cart_items.save()
        return Response({'success': 'Item Modified in the cart'})
    
    def delete(self, request):
        data = request.data
        user = request.user
        cart_items = CartItem.objects.get(id = data.get('id'))
        price_old_item = cart_items.price
        cart_items.delete()

        cart = Cart.objects.filter(user=user, ordered=False).first()
        cart.total_price -= price_old_item # update the total price of cart
        cart.save()
        queryset = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(queryset, many=True)
        return Response({'success': 'Item Deleted from Cart', 'count': len(serializer.data), 'data': serializer.data})