from django.shortcuts import render
from .models import electricBicycle
from .models import productsInfo
from .models import BikesDetails
from .models import BikeImage
# Create your views here.

def homepage(request):
    product = electricBicycle.objects.all()
    return render(request, 'products/homepage.html', {'products': product})
def products(request):
    products = productsInfo.objects.all()
    return render(request, 'products/product.html', {'products': products})
def Pagebikes(request, id):
    bikes = BikesDetails.objects.get(id=id)
    bikeImage = BikeImage.objects.filter(bike=bikes)
    context = {
        'productDetails': bikes,
        'bikesImage' : bikeImage
    }
    return render(request, 'products/product_detail.html', context)
