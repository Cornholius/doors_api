from unicodedata import name
from import_export import resources, fields
from .models import Door, Collection, Company
from import_export.widgets import ForeignKeyWidget
from collections import OrderedDict


class DoorsResource(resources.ModelResource):
    name = fields.Field(column_name='Название', attribute='name')
    company = fields.Field(column_name='Компания', attribute='company', widget=ForeignKeyWidget(Company, 'company_name'))
    collection = fields.Field(column_name='Коллекция', attribute='collection', widget=ForeignKeyWidget(Collection, 'collection_name'))
    description = fields.Field(column_name='Описание', attribute='description')
    canvas = fields.Field(column_name='Полотно', attribute='canvas')
    exterior_decoration = fields.Field(column_name='Наружная отделка', attribute='exterior_decoration')
    interior_decoration = fields.Field(column_name='Внутренняя отделка', attribute='interior_decoration')
    color = fields.Field(column_name='Цвет покраски', attribute='color')
    weight = fields.Field(column_name='Вес образца', attribute='weight')
    photo = fields.Field(column_name='Фото двери', attribute='photo')


    class Meta:
        model = Door
    
    def before_import_row(row, *args, **kwargs):
        '''
        Функция проверки наличия компаний и коллекций в БД. При их отсутствии создаёт цепочку компания - коллекция
        '''
        incoming_row = OrderedDict(args[0])
        (company, collection) = incoming_row['Компания'], incoming_row['Коллекция']
        check_company = Company.objects.get_or_create(company_name=company)
        check_collection = Collection.objects.get_or_create(collection_name=collection, company=check_company[0])
  