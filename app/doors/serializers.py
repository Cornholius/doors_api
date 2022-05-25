from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'url', 'name')


class CollectionSerializer(serializers.HyperlinkedModelSerializer):

    company = serializers.StringRelatedField()

    class Meta:
        model = Collection
        fields = ('id', 'url', 'company', 'name')


class DoorSerializer(serializers.HyperlinkedModelSerializer):

    collection = serializers.StringRelatedField()

    class Meta:
        model = Door
        fields = (
            'id',
            'url',
            'collection',
            'name',
            )
