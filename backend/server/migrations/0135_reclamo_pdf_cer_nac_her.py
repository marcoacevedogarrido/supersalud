# Generated by Django 3.0.5 on 2020-04-21 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0134_reclamo_hecho_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='reclamo',
            name='pdf_cer_nac_her',
            field=models.FileField(blank=True, null=True, upload_to='Escritorio/'),
        ),
    ]
