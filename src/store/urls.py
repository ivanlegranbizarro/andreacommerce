from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('api/', views.ItemsListView.as_view(), name='store'),
    path('api/item/<pk>/', views.ItemDetailView.as_view(), name='item-detail'),
    path('api/order-items/<pk>', views.OrderItemView.as_view(), name='order-items'),
    path('api/order/<pk>/', views.OrderView.as_view(), name='order'),
    path('api/orders', views.AllOrdersView.as_view(), name='all-orders'),
]
