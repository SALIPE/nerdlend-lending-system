# Generated by Django 5.1.3 on 2024-11-20 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favorite',
            new_name='Tbfavorite',
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Tbproduct',
        ),
    ]
