# Generated by Django 5.0.1 on 2024-01-14 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageDough', '0003_alter_inventoryraw_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calcs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversion', models.FloatField()),
                ('base', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base', to='manageDough.unit')),
                ('one_to_convert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='one_to_convert', to='manageDough.unit')),
            ],
        ),
    ]
