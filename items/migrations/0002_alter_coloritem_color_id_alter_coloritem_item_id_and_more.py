# Generated by Django 5.1.2 on 2024-12-10 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coloritem',
            name='color_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='coloritem',
            name='item_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='materialitem',
            name='item_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='materialitem',
            name='material_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shapeitem',
            name='item_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shapeitem',
            name='shape_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tagitem',
            name='item_id',
            field=models.IntegerField(),
        ),
    ]
