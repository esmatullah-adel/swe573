# Generated by Django 5.1.2 on 2024-12-05 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Color',
            },
        ),
        migrations.CreateModel(
            name='ColorItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=255)),
                ('color_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ColorItem',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('item_id', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255, null=True)),
                ('date', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Condition',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Currency',
            },
        ),
        migrations.CreateModel(
            name='Hardness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Hardness',
            },
        ),
        migrations.CreateModel(
            name='LengthUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'LengthUnit',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Material',
            },
        ),
        migrations.CreateModel(
            name='MaterialItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=255)),
                ('material_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'MaterialItem',
            },
        ),
        migrations.CreateModel(
            name='Shape',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'Shape',
            },
        ),
        migrations.CreateModel(
            name='ShapeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=255)),
                ('shape_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'ShapeItem',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('tag_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='TagItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.CharField(max_length=255)),
                ('tag_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'TagItem',
            },
        ),
        migrations.CreateModel(
            name='WeightUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
            ],
            options={
                'db_table': 'WeightUnit',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
                ('functionality', models.CharField(max_length=255, null=True)),
                ('taste', models.CharField(max_length=255, null=True)),
                ('smell', models.CharField(max_length=255, null=True)),
                ('age', models.CharField(max_length=255, null=True)),
                ('width', models.IntegerField(default=0)),
                ('length', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('weight_unit_id', models.IntegerField(default=1)),
                ('price', models.IntegerField(default=0)),
                ('currency_id', models.IntegerField(default=1)),
                ('hardness_id', models.IntegerField(default=1)),
                ('condition_id', models.IntegerField(default=1)),
                ('image', models.ImageField(blank=True, default='fallback.png', upload_to='')),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('length_unit', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='items.lengthunit')),
            ],
            options={
                'db_table': 'Item',
            },
        ),
    ]
