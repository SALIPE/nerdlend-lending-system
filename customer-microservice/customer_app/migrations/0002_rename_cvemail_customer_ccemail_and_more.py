# Generated by Django 5.1.4 on 2024-12-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='cvemail',
            new_name='ccemail',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='cvname',
        ),
        migrations.AddField(
            model_name='customer',
            name='ccname',
            field=models.CharField(default='Customer', max_length=100, unique=True),
        ),
    ]
