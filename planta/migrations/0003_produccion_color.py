# Generated by Django 4.0.6 on 2022-08-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0002_categoria_producto_produccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
