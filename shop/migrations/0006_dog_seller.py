# Generated by Django 5.0.7 on 2024-09-24 06:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_delivery_address_order_payment_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='seller',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.sellerprofile'),
        ),
    ]
