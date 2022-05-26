from dataclasses import field
from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # fields = ('id', 'url', 'company_name')
        fields = '__all__'


class CollectionSerializer(serializers.HyperlinkedModelSerializer):

    company = serializers.StringRelatedField()

    class Meta:
        model = Collection
        fields = '__all__'
        # fields = ('id', 'url', 'company', 'collection_name')


class DoorSerializer(serializers.HyperlinkedModelSerializer):

    collection = serializers.StringRelatedField()

    class Meta:
        model = Door
        fields = '__all__'
