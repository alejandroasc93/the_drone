# Generated by Django 4.0.3 on 2022-03-06 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0001_initial'),
        ('drones', '0003_alter_drone_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicinesLoadedByDrones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_date', models.DateTimeField(auto_now_add=True, verbose_name='Load date')),
                ('delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='Delivery date')),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drones.drone', verbose_name='drone')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medications.medication', verbose_name='medication')),
            ],
            options={
                'verbose_name': 'MedicinesLoadedByDrone',
                'verbose_name_plural': 'MedicinesLoadedByDrones',
                'db_table': 'tbl_medicines_loaded_by_drones',
            },
        ),
    ]
