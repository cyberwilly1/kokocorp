# Generated by Django 3.2 on 2021-05-31 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='descripcion',
        ),
    ]
