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