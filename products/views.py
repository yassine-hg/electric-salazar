from django.shortcuts import render
from .models import electricBicycle
from .models import productsInfo
from .models import BikesDetails
from .models import BikeImage
from .models import batterie
from .models import batterie_image
from .models import trotinette_electrique
from .models import trotinette_image
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

def batteries_page(request):
    batterie_element = batterie.objects.all()
    return render(request, 'products/batterie.html', {'batterie_element': batterie_element}) 

def batterie_elements(request, id):
    batterie_info = batterie.objects.get(id=id)
    batterie_image_detail = batterie_image.objects.filter(batterie=batterie_info) 
    context = {
        'batterie_info': batterie_info,
        'batterie_image_detail': batterie_image_detail
    }
    return render(request, 'products/batterie_details.html', context)
def trotinette_page(request):
    trotinette_element = trotinette_electrique.objects.all()
    return render(request, 'products/trotinette.html', {'trotinette_element': trotinette_element})
def trotinette_elements(request, id):
    trotinettes = trotinette_electrique.objects.get(id=id)
    trotinette_images = trotinette_image.objects.filter(trotinette=trotinettes)
    context = {
        'trotinettes': trotinettes,
        'trotinette_images' : trotinette_images
    }
    return render(request, 'products/trotinette_details.html', context)