# Generated by Django 3.1.6 on 2021-03-17 17:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0004_auto_20210317_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ingredients', models.ManyToManyField(to='recipe.Ingredients')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
        ),
    ]
