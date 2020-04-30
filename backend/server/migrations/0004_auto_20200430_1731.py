# Generated by Django 2.2.6 on 2020-04-30 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20200429_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instancia',
            name='afectado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instancias_afectado', to='server.Afectado'),
        ),
        migrations.AlterField(
            model_name='instancia',
            name='representante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instancias_representante', to='server.Representante'),
        ),
    ]
