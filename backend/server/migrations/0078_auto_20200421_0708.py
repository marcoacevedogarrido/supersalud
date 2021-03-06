# Generated by Django 3.0.5 on 2020-04-21 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0077_reclamante_digitoverificador'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='tipo_beneficiario',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='sub_materia1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='sub_materia2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reclamo',
            name='sub_materia3',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
