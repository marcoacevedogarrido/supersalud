# Generated by Django 2.2.6 on 2020-04-28 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Afectado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField(blank=True, null=True)),
                ('dv', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('edad', models.IntegerField(null=True)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('tipo_pac', models.BooleanField(null=True)),
                ('fallece_pac', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Archivos_ECM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proceso', models.CharField(max_length=50, null=True)),
                ('type', models.CharField(choices=[('s3', 'S3'), ('alfresco', 'Alfresco'), ('dspace', 'Dspace')], max_length=20)),
                ('link_descarga', models.URLField(blank=True, null=True)),
                ('id_repositorio', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Aseguradora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_isapre', models.CharField(max_length=50, null=True)),
                ('codigo_isapre', models.IntegerField(null=True)),
                ('nombre_isapre_corto', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_comuna', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cotizante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField(blank=True, null=True)),
                ('dv', models.CharField(blank=True, max_length=50, null=True)),
                ('nombres', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono_contacto_uno', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_contacto_dos', models.CharField(blank=True, max_length=50, null=True)),
                ('correo_electronico', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion_nombre_calle', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion_numero_calle', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion_departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('aseguradora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizantes_aseguradora', to='server.Aseguradora')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizantes_comuna', to='server.Comuna')),
            ],
        ),
        migrations.CreateModel(
            name='Datos_camunda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idDeployment', models.CharField(blank=True, max_length=60, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('source', models.CharField(blank=True, max_length=50, null=True)),
                ('deploymentTime', models.DateTimeField()),
                ('tenantId', models.IntegerField(null=True)),
                ('deployedProcessDefinitions', models.CharField(blank=True, max_length=60, null=True)),
                ('deployedCaseDefinitions', models.CharField(blank=True, max_length=60, null=True)),
                ('deployedDecisionDefinitions', models.CharField(blank=True, max_length=60, null=True)),
                ('deployedDecisionRequirementsDefinitions', models.CharField(blank=True, max_length=60, null=True)),
                ('key', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Estado_Plantilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_genero', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Instancia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_json', models.TextField(null=True)),
                ('n_reclamo', models.CharField(max_length=100)),
                ('descripcion_problema', models.TextField()),
                ('explicacion', models.TextField()),
                ('es_reclamante_y_afectado', models.BooleanField(default=False)),
                ('notificacion_electronica', models.BooleanField(default=False)),
                ('correo_electronico_notificacion', models.CharField(blank=True, max_length=50, null=True)),
                ('comentarios', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_limite', models.DateField()),
                ('folio', models.CharField(blank=True, max_length=50, null=True)),
                ('triage', models.CharField(blank=True, max_length=50, null=True)),
                ('canal_ingreso', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_reclamo_prestador', models.DateField()),
                ('fecha_carta_respuesta', models.DateField()),
                ('fecha_limite_respuesta_prestador', models.DateField()),
                ('fecha_inicio_para_prestar_reclamo', models.DateField()),
                ('fecha_fin_para_prestar_reclamo', models.DateField()),
                ('fecha_desde', models.DateField()),
                ('fecha_hasta', models.DateField()),
                ('afectado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_afectado', to='server.Afectado')),
                ('aseguradora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_aseguradora', to='server.Aseguradora')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_comuna', to='server.Comuna')),
                ('cotizante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_cotizante', to='server.Cotizante')),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(null=True)),
                ('gentilicio', models.CharField(default='Chileno/a', max_length=50)),
                ('nombre', models.CharField(default='Chile', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('filename', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('version', models.CharField(blank=True, max_length=50, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantillas_estado', to='server.Estado_Plantilla')),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Process_Definition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_camunda', models.CharField(max_length=100)),
                ('key', models.CharField(blank=True, max_length=50, null=True)),
                ('category', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('resource', models.CharField(blank=True, max_length=50, null=True)),
                ('deploymentId', models.CharField(blank=True, max_length=50, null=True)),
                ('diagram', models.CharField(blank=True, max_length=50, null=True)),
                ('suspended', models.CharField(blank=True, max_length=50, null=True)),
                ('tenantId', models.CharField(blank=True, max_length=50, null=True)),
                ('versionTag', models.CharField(blank=True, max_length=50, null=True)),
                ('historyTimeToLive', models.CharField(blank=True, max_length=50, null=True)),
                ('startableInTasklist', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_provincia', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_region', models.CharField(max_length=50)),
                ('ordinal', models.IntegerField()),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_sexo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Aseguradora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Calle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Via_Tramitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='via_tramitacion_proceso', to='server.Proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Reclamo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=50, null=True)),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_reclamos_proceso', to='server.Proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=50, null=True)),
                ('sla_dias', models.IntegerField(blank=True, null=True)),
                ('proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas_proceso', to='server.Proceso')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_materias', to='server.Materia')),
            ],
        ),
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.IntegerField(blank=True, null=True)),
                ('dv', models.CharField(blank=True, max_length=50, null=True)),
                ('nombres', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=50, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono_contacto_uno', models.CharField(blank=True, max_length=50, null=True)),
                ('telefono_contacto_dos', models.CharField(blank=True, max_length=50, null=True)),
                ('correo_electronico', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion_nombre_calle', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion_numero_calle', models.CharField(blank=True, max_length=50, null=True)),
                ('direccion_departamento', models.CharField(blank=True, max_length=50, null=True)),
                ('aseguradora', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes_aseguradora', to='server.Aseguradora')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes_comuna', to='server.Comuna')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes_genero', to='server.Genero')),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes_nacionalidad', to='server.Nacionalidad')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes_privincia', to='server.Provincia')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes_region', to='server.Region')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='representantes_sexo', to='server.Sexo')),
            ],
        ),
        migrations.AddField(
            model_name='provincia',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provincias_region', to='server.Region'),
        ),
        migrations.CreateModel(
            name='Process_Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('id_plano', models.CharField(max_length=60, null=True)),
                ('definitionId', models.CharField(max_length=60, null=True)),
                ('businessKey', models.CharField(max_length=60, null=True)),
                ('caseInstanceId', models.CharField(max_length=60, null=True)),
                ('ended', models.BooleanField(default=False)),
                ('suspended', models.BooleanField(default=False)),
                ('tenantId', models.CharField(max_length=60, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='procesos_usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='proceso',
            name='process_definition',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='proceso_process_definition', to='server.Process_Definition'),
        ),
        migrations.CreateModel(
            name='Prestador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestadores_comuna', to='server.Comuna')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestadores_provincia', to='server.Provincia')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prestadores_region', to='server.Region')),
            ],
        ),
        migrations.CreateModel(
            name='Plantillas_Tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plantilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantillas', to='server.Plantilla')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantillas_tareas', to='server.Tarea')),
            ],
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('reclamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_reclamo', to='server.Instancia')),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_tarea', to='server.Tarea')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observaciones_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='materia',
            name='proceso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materias_proceso', to='server.Proceso'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_materia', to='server.Materia'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='prestador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_prestador', to='server.Prestador'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='process_definition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancia_process_definition', to='server.Process_Definition'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_provincia', to='server.Provincia'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_region', to='server.Region'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='representante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_representante', to='server.Representante'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='sub_materia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_sub_materia', to='server.Sub_Materia'),
        ),
        migrations.AddField(
            model_name='instancia',
            name='tipo_reclamo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instancias_tipo_reclamo', to='server.Tipo_Reclamo'),
        ),
        migrations.CreateModel(
            name='Historia_Proceso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('dias_corridos', models.IntegerField()),
                ('dias_habiles', models.IntegerField()),
                ('tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia_procesos_tarea', to='server.Tarea')),
                ('usuario_responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historia_procesos_usuario_responsable', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Datos_Process_Definition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_variable', models.CharField(blank=True, max_length=60, null=True)),
                ('tipo_variable', models.CharField(blank=True, max_length=60, null=True)),
                ('valor_variable', models.CharField(blank=True, max_length=60, null=True)),
                ('id_start', models.CharField(blank=True, max_length=60, null=True)),
                ('instancia_proceso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='instancia_proceso', to='server.Process_Instance')),
            ],
        ),
        migrations.AddField(
            model_name='cotizante',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizantes_genero', to='server.Genero'),
        ),
        migrations.AddField(
            model_name='cotizante',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizantes_nacionalidad', to='server.Nacionalidad'),
        ),
        migrations.AddField(
            model_name='cotizante',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizantes_provincia', to='server.Provincia'),
        ),
        migrations.AddField(
            model_name='cotizante',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizantes_region', to='server.Region'),
        ),
        migrations.AddField(
            model_name='cotizante',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cotizantes_sexo', to='server.Sexo'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunas_provincia', to='server.Provincia'),
        ),
        migrations.AddField(
            model_name='afectado',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='afectados', to='server.Genero'),
        ),
        migrations.AddField(
            model_name='afectado',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='afectados', to='server.Sexo'),
        ),
    ]
