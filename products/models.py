from django.db import models
from django.db.models import CASCADE

# Create your models here.

class electricBicycle(models.Model):
    name  = models.TextField(max_length=30)
    description = models.TextField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class productsInfo(models.Model):
    image = models.ImageField(upload_to='product_images/')
    name = models.TextField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name
    
class BikesDetails(models.Model):
    image = models.ImageField(upload_to='bikesdetails')
    Description = models.TextField(max_length=455)
    technicalDescription = models.TextField(max_length=255)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    def __str__(self):
        return self.Description
    
class BikeImage(models.Model):
    image = models.ImageField(upload_to="Bike image")
    bike = models.ForeignKey(BikesDetails, on_delete=CASCADE)
    
    def __str__(self):
        return str(self.image)

    

