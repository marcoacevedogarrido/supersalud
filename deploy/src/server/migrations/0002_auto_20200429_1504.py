# Generated by Django 2.2.6 on 2020-04-29 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipo_Prioridad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='instancia',
            name='complaintId',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='instancia',
            name='origen_reclamo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='instancia',
            name='triage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instancias_prioridad', to='server.Tipo_Prioridad'),
        ),
    ]
