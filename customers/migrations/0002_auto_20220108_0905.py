# Generated by Django 3.2.7 on 2022-01-08 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cust_password',
            field=models.CharField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='customer',
            name='cust_username',
            field=models.CharField(default='hi', max_length=200),
        ),
    ]
