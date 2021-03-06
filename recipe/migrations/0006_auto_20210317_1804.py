# Generated by Django 3.1.6 on 2021-03-17 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_buyeruser'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='ingredients',
            field=models.ManyToManyField(to='recipe.Ingredients'),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='BuyerUser',
        ),
    ]
