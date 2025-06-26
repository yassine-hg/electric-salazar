from django.urls import path
from . import views

urlpatterns = [
    path("cart/add/<str:product_type>/<int:product_id>/", views.Add_to_Cart, name="add_cart"),
    path("cart/", views.cart_page, name="cart_page"),
    path("cart/update/<int:item_id>/", views.update_cart_quantity, name="update_cart_quantity"),
    path("cart/delete/<int:item_id>/", views.delete_item, name="delete_item"),
]