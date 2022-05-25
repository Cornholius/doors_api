from unicodedata import name
from django.db import models


class Company(models.Model):
    
    name = models.CharField(max_length=50, verbose_name='Компания')

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __str__(self):
        return self.name


class Collection(models.Model):
    
    company = models.ForeignKey(Company, related_name='test1', verbose_name='Компания', on_delete=models.CASCADE)
    name = models.CharField(max_length=80, verbose_name='Название коллекции')
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name


class Door(models.Model):
    
    collection = models.ForeignKey(Collection, related_name='test2', verbose_name='Коллекция', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Название модели')

    class Meta:
        verbose_name = 'Дверь'
        verbose_name_plural = 'Двери'

    def __str__(self):
        return self.name

