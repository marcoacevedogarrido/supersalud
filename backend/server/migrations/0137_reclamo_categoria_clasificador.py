# Generated by Django 3.0.5 on 2020-04-21 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0136_auto_20200421_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='categoria_clasificador',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
