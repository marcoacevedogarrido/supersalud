# Generated by Django 3.0.5 on 2020-04-21 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0092_reclamo_sexoreclamante'),
    ]

    operations = [
        migrations.AddField(
            model_name='representante',
            name='apellido_materno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='representante',
            name='apellido_paterno',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='representante',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
