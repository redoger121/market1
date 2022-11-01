from django.urls import path

from basketapp.views import *

urlpatterns=[
    path('', basket, name='view'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>/', basket_remove, name='remove'),
    path('edit/<int:pk>/<int:nights>/', basket_edit, name='edit'),
]