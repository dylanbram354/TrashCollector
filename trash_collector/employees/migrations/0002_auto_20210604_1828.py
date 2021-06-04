# Generated by Django 3.1.8 on 2021-06-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]