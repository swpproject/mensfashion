# Generated by Django 3.2.9 on 2021-12-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_cancelorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancelorder',
            name='oid',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
