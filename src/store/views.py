from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

# Create your views here.


class ItemsListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Item.objects.all()
    serializer_class = serializers.ItemSerializer


class OrderItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.OrderItem.objects.all()
    serializer_class = serializers.OrderItemSerializer


class OrderView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class AllOrdersView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
