from rest_framework import serializers
from . import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['id', 'title', 'price', 'description', 'image']


class OrderItemSerializer(serializers.ModelSerializer):
    item = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = models.OrderItem
        fields = ['customer', 'ordered', 'item', 'quantity', 'final_price']

    def get_item(self, obj):
        return ItemSerializer(obj.item).data

    def get_final_price(self, obj):
        return obj.get_final_price()


class OrderSerializer(serializers.ModelSerializer):
    order_items = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = ['customer', 'id', 'items', 'shipping_address', 'paid',
                  'sent', 'received', 'channels', 'order_items', 'total']

    def get_order_items(self, obj):
        return OrderItemSerializer(obj.items.all(),  many=True).data

    def get_total(self, obj):
        return obj.get_total()
