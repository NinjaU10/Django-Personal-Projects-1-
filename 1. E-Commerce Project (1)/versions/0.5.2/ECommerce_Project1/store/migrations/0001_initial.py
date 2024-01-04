# Generated by Django 4.2.5 on 2023-11-20 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='product_pics')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('price', models.FloatField()),
                ('discount', models.IntegerField()),
                ('score', models.FloatField()),
            ],
        ),
    ]