from django.contrib import admin
from .models import CartItem
from .models import Order
from .models import orderItem

admin.site.register(CartItem)

admin.site.register(orderItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'client_name', 'created_at', 'total', 'status')