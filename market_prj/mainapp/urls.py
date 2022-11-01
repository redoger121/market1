from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import *

urlpatterns = [
    path('', accommodations, name='index'),
    path('accommodation_detail/<int:pk>/,', accommodation, name='accommodation'),

]
