# Generated by Django 3.1.7 on 2021-04-05 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0011_auto_20210401_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='cartingredient',
            name='recipe',
        ),
    ]
