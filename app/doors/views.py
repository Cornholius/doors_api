from django.shortcuts import redirect
from django.views import View
from .models import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import *


class DeleteItemView(View):
    """
    Кнопка 'удалить' из админ панели
    """
    
    def get(self, request, type=None, id=None):
        
        item_type = {
            'company': Company,
            'collection': Collection,
            'door': Door,

        }

        item = item_type[type].objects.get(id=id)
        item.delete()

        return redirect(f'/admin/doors/{type}/')


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    http_method_names = ['get']

class CollectionViewSet(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    http_method_names = ['get']


class DoorsViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer
    http_method_names = ['get']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['collection__collection_name']
