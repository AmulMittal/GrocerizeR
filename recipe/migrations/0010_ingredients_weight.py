# Generated by Django 3.1.6 on 2021-03-22 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0009_auto_20210319_0656'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='weight',
            field=models.FloatField(default=10),
            preserve_default=False,
        ),
    ]