from import_export import resources, fields
from .models import Door, Collection, Company
from import_export.widgets import ForeignKeyWidget


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
        # exclude = ['id']
        # import_id_fields = ['area_number']
        # fields = ('collection',)