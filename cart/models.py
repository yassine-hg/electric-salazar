from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from products.models import BikesDetails
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    quantity = models.IntegerField(default=1)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    client_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(max_length=20, default="Nouveau")

    def __str__(self):
        return self.client_name
    
class orderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE, related_name="item" )
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveBigIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product_name