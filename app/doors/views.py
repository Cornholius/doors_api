from django.shortcuts import redirect
from django.views import View
from .models import *
from rest_framework import viewsets
from .serializers import *

class DeleteItemView(View):

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


class DoorViewSet(viewsets.ModelViewSet):
    queryset = Door.objects.all()
    serializer_class = DoorSerializer
    http_method_names = ['get']
