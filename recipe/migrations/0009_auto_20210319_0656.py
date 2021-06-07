# Generated by Django 3.1.6 on 2021-03-19 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0008_auto_20210317_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='recipe',
            field=models.ManyToManyField(blank=True, null=True, to='recipe.Recipe'),
        ),
        migrations.RemoveField(
            model_name='mycookbook',
            name='recipe',
        ),
        migrations.AddField(
            model_name='mycookbook',
            name='recipe',
            field=models.ManyToManyField(blank=True, null=True, to='recipe.Recipe'),
        ),
    ]
