# basic-ecommerce-app

## Used simple JWT , for authentication of each user adding a new item in cart 
```
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
```
## Used serializers to see the data as a JSON 
```
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

```

## Used the signals like post_save , pre_save , post_delete to update the total cart price
```
@receiver(pre_save, sender=CartItem)
def update_price(sender, **kwargs):
    # update price of cart_item

    cart_item = kwargs['instance']
    product = Product.objects.get(id=cart_item.product.id)
    cart_item.price = int(cart_item.quantity) * float(product.price)
    print( cart_item.quantity, float(product.price))

@receiver(post_save, sender=CartItem)
def update_total_price(sender, **kwargs):
    cart_item = kwargs['instance']
    # update total_price of Cart
    cart = Cart.objects.get(id=cart_item.cart.id)
    total_price = 0.0
    cart_item = CartItem.objects.filter(cart__id = cart.id)
    print(cart_item)
    for item in cart_item:
        total_price += item.price
    cart.total_price = total_price
    cart.save()```

