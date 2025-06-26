from django.shortcuts import render, redirect, get_object_or_404
from products.models import BikesDetails
from products.models import batterie
from .models import CartItem
from django.contrib.contenttypes.models import ContentType

def Add_to_Cart(request, product_type, product_id):
    model_map = {
        'bike': BikesDetails,
        'batterie': batterie,
    }
    model = model_map.get(product_type)
    if not model:
        return redirect('bike')
    product = model.objects.get(id = product_id)
    content_type = ContentType.objects.get_for_model(model)
    cart_item , created = CartItem.objects.get_or_create(
        user=request.user,
        content_type=content_type,
        object_id=product.id,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_page')


def cart_page(request):
    total_price = 0
    cart_items = CartItem.objects.filter(user=request.user)
    for item in cart_items:
        total_price += item.content_object.price * item.quantity
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})


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
            total_price += item.content_object.price * item.quantity 
    return redirect('cart_page')


