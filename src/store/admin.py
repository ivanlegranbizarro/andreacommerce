from django.contrib import admin
from .models import (
    Customer,
    Item,
    OrderItem,
    Order
)
# Register your models here.


admin.site.register([Customer, Item, OrderItem, Order])
