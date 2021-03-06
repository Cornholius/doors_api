# Generated by Django 4.0.4 on 2022-05-25 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0004_door_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='name',
            field=models.CharField(max_length=80, unique=True, verbose_name='Название коллекции'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Компания'),
        ),
        migrations.AlterField(
            model_name='door',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='name1', to='doors.collection', verbose_name='Коллекция'),
        ),
    ]
