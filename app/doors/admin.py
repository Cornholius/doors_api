from django.contrib import admin
from .models import *


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):

    def company(self, obj):
        return obj.name

    list_display = ('name', 'company')


@admin.register(Door)
class DoorAdmin(admin.ModelAdmin):

    list_display = ('name', 'collection')
    
    def collection(self, obj):
        return obj.name
    
    collection.short_description = 'Коллекция'
    
