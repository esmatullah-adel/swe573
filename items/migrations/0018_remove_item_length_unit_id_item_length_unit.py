# Generated by Django 5.1.2 on 2024-12-04 06:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_rename_massunit_weightunit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='length_unit_id',
        ),
        migrations.AddField(
            model_name='item',
            name='length_unit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.lengthunit'),
        ),
    ]
