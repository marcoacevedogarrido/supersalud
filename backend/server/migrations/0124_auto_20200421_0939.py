# Generated by Django 3.0.5 on 2020-04-21 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0123_reclamo_hecho_mes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reclamo',
            old_name='notificacion',
            new_name='notificar_tramite_id',
        ),
    ]