# Generated by Django 5.2 on 2025-04-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='electricBicycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('description', models.TextField(max_length=255)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
