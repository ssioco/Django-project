# Generated by Django 4.0.6 on 2022-08-02 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planta', '0004_remove_produccion_color_producto_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='color',
            field=models.CharField(choices=[('rojo', 'ROJO'), ('verde', 'VERDE'), ('azul', 'AZUL')], default='r', max_length=100),
        ),
    ]
