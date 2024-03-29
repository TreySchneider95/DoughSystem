# Generated by Django 5.0.1 on 2024-01-11 17:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryRaw',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('qty', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('amount_made', models.FloatField()),
                ('person_made', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dough',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('date_made', models.DateField(auto_now=True)),
                ('price_per_scoop', models.FloatField()),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='manageDough.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngrediant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageDough.inventoryraw')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageDough.recipe')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageDough.unit')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='manageDough.RecipeIngrediant', to='manageDough.inventoryraw'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='amount_made_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageDough.unit'),
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_purchased', models.DateField()),
                ('price', models.FloatField()),
                ('where', models.CharField(max_length=200)),
                ('qty_purchased', models.FloatField()),
                ('qty_left', models.FloatField()),
                ('refrigerated', models.BooleanField()),
                ('person_who_purchased', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageDough.inventoryraw')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageDough.unit')),
            ],
        ),
        migrations.AddField(
            model_name='inventoryraw',
            name='unit_used',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manageDough.unit'),
        ),
    ]
