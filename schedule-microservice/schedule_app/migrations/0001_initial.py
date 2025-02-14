# Generated by Django 5.1.3 on 2024-11-22 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('cv_id', models.AutoField(primary_key=True, serialize=False)),
                ('cv_product_id', models.IntegerField()),
                ('cv_schedule_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('cv_id', models.AutoField(primary_key=True, serialize=False)),
                ('cv_customer_id', models.IntegerField()),
                ('cd_with_draw_date', models.DateField()),
                ('cd_due_date', models.DateField()),
                ('cb_returned_date', models.DateField(blank=True, null=True)),
                ('cv_value', models.DecimalField(decimal_places=2, max_digits=18)),
                ('cd_create_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
