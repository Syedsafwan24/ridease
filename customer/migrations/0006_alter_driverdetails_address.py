# Generated by Django 5.0.2 on 2024-04-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_riderequest_driverdetails_ride_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverdetails',
            name='address',
            field=models.CharField(max_length=150),
        ),
    ]
