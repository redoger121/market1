from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import include

import mainapp.views as mainapp


urlpatterns = [
    path('admin/', include(('adminapp.urls', 'admin'))),
    path('', mainapp.main, name='main'),
    path('list_of_accommodations/', include(('mainapp.urls', 'acc'))),
    path('auth/', include(('authapp.urls', 'auth'))),
    path('', include(('social_django.urls', 'social'))),
    path('basket/', include(('basketapp.urls', 'basket'))),
    path('order/', include(('ordersapp.urls', 'ordersapp'))),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )