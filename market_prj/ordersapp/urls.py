from ordersapp.views import *
from django.urls import path



urlpatterns=[
    path('', OrderList.as_view(), name='orders_list'),
    path('create/', OrderItemsCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', OrderItemsUpdate.as_view(), name='order_update'),
    path('read/<int:pk>/', OrdeRead.as_view(), name='order_read'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),

]



