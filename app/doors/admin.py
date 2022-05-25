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
    delete_button.short_description = ''


@admin.register(Door)

class DoorAdmin(ImportExportActionModelAdmin):
    
    resource_class = DoorsResource

    def before_import(dataset, using_transactions, dry_run, **kwargs):
        print('>>>>>>>>>>>>>>>', dataset)
    # def before_import_row(self, row, **kwargs):
    #     company = row.get('company')
    #     collection = row.get('collection')
    #     print('>>>>>>>>>>>>>>>>>>>>>>>>>', company, collection)
    #     (comp, _created) = Company.objects.get_or_create(name=company)
    #     (coll, _created) = Collection.objects.get_or_create(name=collection, company=comp)
    #     row['collection'] = coll.name

    # def collection(self, obj):
    #     return obj.name

    def delete_button(self, obj):
        return format_html('<a class="AdminDeleteBtn" href="/delete/door/{}/">Удалить</a>', obj.id)
    
    # list_display = ()
    # list_display = "__all__"
    delete_button.short_description = ''

