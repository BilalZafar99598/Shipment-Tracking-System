# Generated by Django 3.2.9 on 2022-03-24 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_shipment_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipment',
            name='status',
        ),
    ]
