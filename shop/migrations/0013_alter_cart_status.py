# Generated by Django 3.2.9 on 2021-12-13 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_rename_geeks_field_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('In Process', 'In Process'), ('Packing', 'Packing'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Return', 'Return')], default='In Process', max_length=100),
        ),
    ]
