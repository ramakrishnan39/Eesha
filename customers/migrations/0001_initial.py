# Generated by Django 3.2.7 on 2022-01-06 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(blank=True, max_length=50, null=True)),
                ('cust_phone', models.IntegerField(blank=True, null=True)),
                ('cust_address', models.CharField(max_length=500)),
                ('cust_email', models.CharField(max_length=50)),
                ('cust', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
