# Generated by Django 3.1.6 on 2021-03-17 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20210317_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total_ingredient',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total_recipe',
        ),
    ]