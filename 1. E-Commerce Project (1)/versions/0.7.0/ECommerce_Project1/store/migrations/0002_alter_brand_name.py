# Generated by Django 5.0.1 on 2024-03-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(default='N', max_length=255),
        ),
    ]
