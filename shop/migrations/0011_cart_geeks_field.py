# Generated by Django 3.2.9 on 2021-12-13 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_cart_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='geeks_field',
            field=models.CharField(choices=[('In Process', 'In Process'), ('Packing', 'Packing'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Return', 'Return')], default='In Process', max_length=100),
        ),
    ]
