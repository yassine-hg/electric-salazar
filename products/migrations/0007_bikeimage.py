# Generated by Django 5.2 on 2025-05-01 21:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_bikesdetails_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Bike image')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.bikesdetails')),
            ],
        ),
    ]
