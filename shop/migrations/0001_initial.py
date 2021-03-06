# Generated by Django 3.2.9 on 2021-12-07 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('feature', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('description', models.TextField()),
                ('specifications', models.TextField()),
                ('stock', models.IntegerField(default=10)),
                ('img1', models.ImageField(null=True, upload_to='products')),
                ('img2', models.ImageField(null=True, upload_to='products')),
                ('img3', models.ImageField(null=True, upload_to='products')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
