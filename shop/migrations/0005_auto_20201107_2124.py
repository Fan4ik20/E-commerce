# Generated by Django 3.1.3 on 2020-11-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201107_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
