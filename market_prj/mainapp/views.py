from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Accommodation, Regions, ListOfCountries

# Create your views here.


def main(request):
    return render(request, 'mainapp/index.html')


def accommodations(request):
    title = 'Размещение'
    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }
    return render(request, 'mainapp/accommodations.html', content)


def accommodation(request, pk=None):
    title = 'Продукты'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk)
    }
    return render(request, 'mainapp/accommodation_details.html', content)
