# Generated by Django 5.2 on 2025-04-29 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_productsinfo_moreimage_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BikesDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='bikesdetails')),
                ('Description', models.TextField(max_length=455)),
                ('technicalDescription', models.TextField(max_length=255)),
            ],
        ),
    ]
