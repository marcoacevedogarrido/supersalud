# Generated by Django 3.0.5 on 2020-04-21 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0133_reclamo_regionrec'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='hecho_ano',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
