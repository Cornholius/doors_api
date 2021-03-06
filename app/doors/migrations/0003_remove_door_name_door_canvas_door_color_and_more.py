# Generated by Django 4.0.4 on 2022-05-25 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0002_alter_collection_options_alter_company_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='door',
            name='name',
        ),
        migrations.AddField(
            model_name='door',
            name='canvas',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Полотно'),
        ),
        migrations.AddField(
            model_name='door',
            name='color',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Цвет покраски'),
        ),
        migrations.AddField(
            model_name='door',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='door',
            name='exterior_decoration',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Наружная отделка'),
        ),
        migrations.AddField(
            model_name='door',
            name='interior_decoration',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Внутренняя отделка'),
        ),
        migrations.AddField(
            model_name='door',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='doors_img/', verbose_name='Фото двери'),
        ),
        migrations.AddField(
            model_name='door',
            name='weight',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='Вес образца'),
        ),
        migrations.AlterField(
            model_name='door',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test2', to='doors.collection', verbose_name='Коллекция'),
        ),
    ]
