# Generated by Django 3.0.5 on 2020-04-20 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0067_representante_reclamante'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='representante',
            field=models.OneToOneField(blank=True, default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reclamos', to='server.Representante'),
        ),
    ]
