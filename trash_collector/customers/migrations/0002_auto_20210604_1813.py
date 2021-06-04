# Generated by Django 3.1.8 on 2021-06-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='balance',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='onetime_pickup',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='pickup_day',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='suspension_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='suspension_start',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
