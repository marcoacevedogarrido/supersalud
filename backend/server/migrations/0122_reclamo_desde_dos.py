# Generated by Django 3.0.5 on 2020-04-21 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0121_reclamo_comunarep'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='desde_dos',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
