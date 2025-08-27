from django.shortcuts import render, redirect, get_object_or_404
from products.models import BikesDetails
from products.models import batterie
from products.models import trotinette_electrique
from .models import CartItem
from .models import Order
from .models import orderItem
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
import urllib.parse

def Add_to_Cart(request, product_type, product_id):
    model_map = {
        'bike': BikesDetails,
        'batterie': batterie,
        'trotinette' : trotinette_electrique,
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

import urllib.parse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def commander_panier(request):
    user = request.user
    nom_client = f"{user.first_name} {user.last_name}".strip() or user.username

    numero_whatsapp = '212682647991'
    message = f"Bonjour, je suis {nom_client}, je viens de passer une commande sur Electric Sazale."
    wa_link = f"https://wa.me/{numero_whatsapp}?text={urllib.parse.quote(message)}"

    if request.method == 'POST':
        return redirect(wa_link)
    return redirect('cart_page')  
def confirmation_page(request):
    return render(request, 'confirmation.html')

def OrderStore(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total = 0

    for item in cart_items:
        total += item.content_object.price * item.quantity

    order = Order.objects.create(
        user=user,
        client_name=f"{user.first_name} {user.last_name}",
        total=total,
        status="Nouveau"
    )

    for item in cart_items:
        orderItem.objects.create(
            order=order,
            product_name=str(item.content_object),  
            quantity=item.quantity,
            price=item.content_object.price
        )

    cart_items.delete()

    return redirect('confirmation_page')
