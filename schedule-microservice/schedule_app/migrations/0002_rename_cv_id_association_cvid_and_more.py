# Generated by Django 5.1.4 on 2025-01-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='association',
            old_name='cv_id',
            new_name='cvid',
        ),
        migrations.RenameField(
            model_name='association',
            old_name='cv_product_id',
            new_name='cvproductid',
        ),
        migrations.RenameField(
            model_name='association',
            old_name='cv_schedule_id',
            new_name='cvscheduleid',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='cd_create_date',
            new_name='cdcreatedate',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='cb_returned_date',
            new_name='cdduedate',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='cv_customer_id',
            new_name='cvcustomerid',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='cv_id',
            new_name='cvid',
        ),
        migrations.RenameField(
            model_name='schedule',
            old_name='cv_value',
            new_name='cvvalue',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='cd_due_date',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='cd_with_draw_date',
        ),
        migrations.AddField(
            model_name='schedule',
            name='cdreturneddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='schedule',
            name='cdwithdrawdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
