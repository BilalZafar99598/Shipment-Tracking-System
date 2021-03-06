# Generated by Django 3.2.9 on 2022-03-24 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_shipment_statuses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipment',
            name='statuses',
            field=models.CharField(choices=[('Ready_for_pickup', 'Ready_for_pickup'), ('pickedup', 'pickedup'), ('In_cargo', 'In_cargo'), ('reached_destination', 'reached_destination'), ('delivered', 'delivered')], default='', max_length=50),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.shipment')),
            ],
        ),
    ]
