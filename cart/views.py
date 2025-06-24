from django.shortcuts import render, redirect, get_object_or_404
from products.models import BikesDetails
from .models import CartItem

def Add_to_Cart(request, product_id):
    bikesDetails = BikesDetails.objects.get(id=product_id)
    cart_items = CartItem.objects.filter(user=request.user, bike=bikesDetails).first()
    if cart_items is None:
        cart_item = CartItem.objects.create(user=request.user, bike=bikesDetails, quantity=1)
    else:
        cart_items.quantity += 1
        cart_items.save()

    return redirect('cart_page')


def cart_page(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = 0
    for item in CartItem.objects.filter(user=request.user):
            total_price += item.bike.price * item.quantity
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price' : total_price})


def update_cart_quantity(request, item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user )
        action = request.POST.get("action")
        if action  == "decrease":
            if cart_item.quantity >  1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        elif action == "increase":
            cart_item.quantity += 1
            cart_item.save()
    return redirect('cart_page')

def delete_item(request, item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        cart_item.delete()
    return redirect('cart_page')

def total_price(request, item_id):
    if request.method == "POST":
        total_price = 0
        for item in CartItem.objects.filter(user=request.user):
            total_price += item.bike.price * item.quantity 
    return redirect('cart_page')


