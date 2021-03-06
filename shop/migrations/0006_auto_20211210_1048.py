# Generated by Django 3.2.9 on 2021-12-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_cart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='order',
            name='firstname',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='order',
            name='lastname',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='order',
            name='mobile',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='order',
            name='paymenttype',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
