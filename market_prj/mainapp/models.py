from django.db import models

# Create your models here.
class ListOfCountries(models.Model):
    name=models.CharField(max_length=64, verbose_name='Имя', unique=True)
    description=models.TextField(verbose_name='Описание', blank=True)
    is_active=models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):
        return self.name

class Regions(models.Model):
    country=models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    name=models.CharField(max_length=64, verbose_name='Имя', unique=True)
    description=models.TextField(verbose_name='Описание', blank=True)
    is_active=models.BooleanField(verbose_name='активна', default=True)


    def __str__(self):
        return self.name

class Accommodation(models.Model):
    country=models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    region=models.ForeignKey(Regions, on_delete=models.CASCADE)
    name=models.CharField(max_length=128, verbose_name='Название проживания', unique=True)
    image=models.ImageField(upload_to='accomodations_img', blank=True)
    short_desc=models.TextField(verbose_name='Краткое описание продукта', max_length=60, blank=True)
    description=models.TextField(verbose_name='Описание продукта', blank=True)
    availability=models.PositiveIntegerField(verbose_name='Количесвто свободных номеров')
    price=models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    room_desc=models.TextField(verbose_name='краткое описание комнаты',max_length=60, blank=True)
    is_active=models.BooleanField(verbose_name='активна', default=True)

    @staticmethod
    def get_items():
        return Accommodation.objects.filter(is_active=True).order_by(
            'country', 'regions', 'name')
    def __str__(self):
        return f'{self.name} ({self.country.name})'
