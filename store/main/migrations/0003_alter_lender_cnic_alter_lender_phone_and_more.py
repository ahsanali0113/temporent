# Generated by Django 4.1 on 2022-08-08 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_lender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lender',
            name='cnic',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lender',
            name='phone',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='lender',
            name='price',
            field=models.CharField(max_length=255),
        ),
    ]
