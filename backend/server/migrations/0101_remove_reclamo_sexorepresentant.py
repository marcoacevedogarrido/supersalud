# Generated by Django 3.0.5 on 2020-04-21 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0100_auto_20200421_0830'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamo',
            name='sexorepresentant',
        ),
    ]
