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
    def __str__(self):
        return self.name
    
class BikesDetails(models.Model):
    name = models.CharField(max_length=455)
    image = models.ImageField(upload_to='bikesdetails')
    kilometrage = models.CharField(max_length=255)
    annee = models.CharField(max_length=255)
    puissance = models.CharField(max_length=255)
    couleur = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class BikeImage(models.Model):
    image = models.ImageField(upload_to="Bike image")
    bike = models.ForeignKey(BikesDetails, on_delete=CASCADE)
    
    def __str__(self):
        return str(self.image)
class batterie(models.Model):
    image = models.ImageField(upload_to="batterie")
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=455)
    price = models.DecimalField(max_digits= 30 , decimal_places=2)
    
    def __str__(self):
        return str(self.name)
class batterie_image(models.Model):
    image = models.ImageField(upload_to= "batterie")
    batterie = models.ForeignKey(batterie, on_delete=CASCADE)
    def __str__(self):
        return str(self.image)
    
class trotinette_electrique(models.Model):
    image = models.ImageField(upload_to="trotinette")
    name = models.TextField(max_length=255)
    description = models.TextField(max_length=455)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    def __str__(self):
        return str(self.name)
    
class trotinette_image(models.Model):
    image = models.ImageField(upload_to="trotinette")
    trotinette = models.ForeignKey(trotinette_electrique, on_delete=CASCADE)
    
    def __str__(self):
        return str(self.image)

    

