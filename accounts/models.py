from django.db import models
# Create your models here.

class imageSignup(models.Model):
    image = models.ImageField()

class ImageOneSign(models.Model):
    storeImage = models.ImageField()
