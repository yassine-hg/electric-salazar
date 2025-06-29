# Generated by Django 5.2 on 2025-06-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_bikeimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='batterie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='batterie')),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=455)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
    ]
