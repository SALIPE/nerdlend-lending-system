# Generated by Django 5.1.4 on 2025-01-10 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trigger_app', '0002_rename_cc_message_trigger_ccmessage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trigger',
            name='ccmessage',
            field=models.TextField(),
        ),
    ]
