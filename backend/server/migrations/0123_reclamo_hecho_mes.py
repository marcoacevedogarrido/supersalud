# Generated by Django 3.0.5 on 2020-04-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0122_reclamo_desde_dos'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='hecho_mes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
