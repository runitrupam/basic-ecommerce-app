from rest_framework import serializers
from .models import *

class QuantityVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuantityVariant
        # fields = '__all__'
        exclude = ['id']


class SizeVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = SizeVariant
        # fields = '__all__'
        exclude = ['id']


class ColorVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorVariant
        # fields = '__all__'
        exclude = ['id']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # fields = '__all__'
        exclude = ['id']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    size_type = SizeVariantSerializer()
    color_type = ColorVariantSerializer()
    qty_type = QuantityVariantSerializer()
    class Meta:
        model = Product
        fields = '__all__'
        # exclude = ['id']