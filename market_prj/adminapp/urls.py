from adminapp.views import *
from django.urls import path


urlpatterns=[
    path('users/read/', TravelUserListView.as_view(),name='users'),
    path('users/create/', user_create, name='user_create'),
    path('users/update/<int:pk>/', update_user, name='user_update'),
    path('users/delete/<int:pk>/', user_delete, name='user_delete'),
    path('countries/read/', countries, name='countries'),
    path('countries/create/', CountryCreateView.as_view(), name='country_create'),
    path('countries/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('countries/delete/<int:pk>/', CountryDeleteView.as_view(), name='country_delete'),
    path('accommodation/read/countries/<int:pk>/', accommodations, name='accommodations'),
    path('accommodations/update/<int:pk>/', accommodation_update, name='accommodation_update'),
    path('accommodations/create/countries/<int:pk>/', accommodation_create, name='accommodation_create'),
    path('accommodations/read/<int:pk>/', AccommodationDetailView.as_view(), name='accommodation_read'),
    path('accommodations/delete/<int:pk>', accommoadtion_delete, name='accommodation_delete'),
]