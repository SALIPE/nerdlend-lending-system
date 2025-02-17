# Generated by Django 5.1.3 on 2024-11-07 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbusertype',
            fields=[
                ('cvid', models.AutoField(primary_key=True, serialize=False)),
                ('ccdescription', models.CharField(blank=True, max_length=45, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tbuser',
            fields=[
                ('cvid', models.AutoField(primary_key=True, serialize=False)),
                ('ccname', models.CharField(blank=True, max_length=45, null=True)),
                ('ccemail', models.EmailField(blank=True, max_length=100, null=True)),
                ('ccpassword', models.CharField(blank=True, max_length=256, null=True)),
                ('cvusertype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='auth_app.tbusertype')),
            ],
        ),
    ]
