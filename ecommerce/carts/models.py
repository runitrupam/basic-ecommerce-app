from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver


# Create your  models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.user) + ' : ' + str(self.total_price)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(default=0.0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.cart.user) + ' : ' + str(self.product.product_name)


@receiver(pre_save, sender=CartItem)
def update_price(sender, **kwargs):
    # update price of cart_item

    cart_item = kwargs['instance']
    product = Product.objects.get(id=cart_item.product.id)
    cart_item.price = int(cart_item.quantity) * float(product.price)
    print(cart_item.quantity, float(product.price))


@receiver(post_save, sender=CartItem)
def update_total_price(sender, **kwargs):
    cart_item = kwargs['instance']
    # update total_price of Cart
    cart = Cart.objects.get(id=cart_item.cart.id)
    total_price = 0.0
    cart_item = CartItem.objects.filter(cart__id=cart.id)
    print(cart_item)
    for item in cart_item:
        total_price += item.price
    cart.total_price = total_price
    cart.save()


# 
# @receiver(pre_delete, sender=CartItem)
# def update_total_price_b(sender, **kwargs):
#     print(kwargs)
# cart_item = kwargs['instance']
# print(cart_item)
# # update total_price of Cart
# cart = Cart.objects.get(id=cart_item.cart.id)
# total_price = 0.0
# cart_item = CartItem.objects.filter(cart__id = cart.id)
# print(cart_item)
# for item in cart_item:
#     total_price += item.price
# cart.total_price = total_price - cart_item.price
# cart.save()


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, blank=True)
    payment_id = models.CharField(max_length=100, blank=True)
    payment_sign = models.CharField(max_length=100, blank=True)


class OrderedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
