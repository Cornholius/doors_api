from distutils.command.upload import upload
from statistics import mode
from types import NoneType
from unicodedata import name
from django.db import models


class Company(models.Model):
    
    company_name = models.CharField(max_length=50, verbose_name='Компания', unique=True)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.company_name


class Collection(models.Model):
    
    company = models.ForeignKey(Company, related_name='test1', verbose_name='Компания', on_delete=models.CASCADE)
    collection_name = models.CharField(max_length=80, verbose_name='Название коллекции', unique=True)
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.collection_name


class Door(models.Model):
    
    door_name = models.CharField(max_length=400, verbose_name='Название', blank=True, null=True)
    collection = models.ForeignKey(Collection, related_name='collections', verbose_name='Коллекция', on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(max_length=5000, verbose_name='Описание', blank=True, null=True)
    canvas = models.CharField(max_length=400, verbose_name='Полотно', blank=True, null=True)
    exterior_decoration = models.CharField(max_length=400, verbose_name='Наружная отделка', blank=True, null=True)
    interior_decoration = models.CharField(max_length=400, verbose_name='Внутренняя отделка', blank=True, null=True)
    color = models.CharField(max_length=400, verbose_name='Цвет покраски', blank=True, null=True)
    weight = models.CharField(max_length=400, verbose_name='Вес образца', blank=True, null=True)
    photo = models.ImageField(upload_to='doors_img/', verbose_name='Фото двери', blank=True, null=True)

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'

    def __str__(self):
        if self.door_name is None:
            return f'Дверь {self.id}'
        else:
            return self.door_name

