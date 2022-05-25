from django.contrib import admin
from .models import *
from django.utils.html import format_html


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    
    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/company/{}/">Удалить</a>', obj.id)

    list_display = ('name', 'delete_button')
    delete_button.short_description = ''


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/collection/{}/">Удалить</a>', obj.id)

    def company(self, obj):
        return obj.name

    list_display = ('name', 'company', 'delete_button')
    delete_button.short_description = ''


@admin.register(Door)
class DoorAdmin(admin.ModelAdmin):

    def collection(self, obj):
        return obj.name

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/door/{}/">Удалить</a>', obj.id)
    
    list_display = ('name', 'collection', 'delete_button')
    delete_button.short_description = ''

