# Generated by Django 2.2.6 on 2020-04-29 21:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20200429_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='ordinal',
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='server.Region'),
        ),
        migrations.AddField(
            model_name='region',
            name='region_ordinal',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='codigo_comuna',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='comuna',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='observacion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='codigo_provincia',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='provincia',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='region',
            name='codigo_region',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='region',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]