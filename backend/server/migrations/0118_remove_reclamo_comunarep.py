# Generated by Django 3.0.5 on 2020-04-21 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0117_representante_comunarep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reclamo',
            name='comunarep',
        ),
    ]
