# Generated by Django 3.0.5 on 2020-04-20 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0066_representante'),
    ]

    operations = [
        migrations.AddField(
            model_name='representante',
            name='reclamante',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='representantes', to='server.Reclamante'),
        ),
    ]