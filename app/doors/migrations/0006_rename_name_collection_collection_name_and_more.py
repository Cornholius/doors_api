# Generated by Django 4.0.4 on 2022-05-25 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doors', '0005_alter_collection_name_alter_company_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collection',
            old_name='name',
            new_name='collection_name',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='door',
            old_name='name',
            new_name='door_name',
        ),
        migrations.AlterField(
            model_name='door',
            name='collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='doors.collection', verbose_name='Коллекция'),
        ),
    ]
