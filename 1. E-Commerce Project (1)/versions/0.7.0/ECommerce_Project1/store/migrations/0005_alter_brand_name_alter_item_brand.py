# Generated by Django 5.0.1 on 2024-03-25 20:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_rename_itemspecs_itemspecvalue_alter_item_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, default='N/A', null=True, on_delete=django.db.models.deletion.CASCADE, to='store.brand'),
        ),
    ]
