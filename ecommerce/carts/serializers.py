from rest_framework import serializers
from .models import *
from products.serializers import *


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
        # exclude = ['id']


class CartItemSerializer(serializers.ModelSerializer):
    cart = CartSerializer()
    product = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'
        # exclude = ['id']

