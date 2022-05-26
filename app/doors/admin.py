from django.contrib import admin
from .models import *
from django.utils.html import format_html
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources, fields
from .resources import DoorsResource


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    
    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/company/{}/">Удалить</a>', obj.id)

    list_display = ('company_name', 'delete_button')
    delete_button.short_description = ''


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/collection/{}/">Удалить</a>', obj.id)

    def company(self, obj):
        return obj.name


    # list_display = '__all__'
    list_display = ('collection_name', 'company', 'delete_button')


@admin.register(Door)


class DoorAdmin(ImportExportActionModelAdmin):
    
    resource_class = DoorsResource

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/door/{}/">Удалить</a>', obj.id)
    
    # list_display = "__all__"


