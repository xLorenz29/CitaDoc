# Generated by Django 5.1.7 on 2025-04-02 15:43

import django.contrib.auth.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=50)),
                ('departamento', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('especialidad', models.CharField(max_length=30)),
                ('telefono', models.PositiveIntegerField(blank=True, null=True)),
                ('numero_colegiado', models.CharField(max_length=20, unique=True)),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_hora', models.DateTimeField()),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado')], default='Pendiente', max_length=20)),
                ('motivo_consulta', models.CharField(blank=True, max_length=100, null=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateTimeField(auto_now_add=True)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('metodo_pago', models.CharField(choices=[('Tarjeta', 'Tarjeta'), ('Efectivo', 'Efectivo'), ('Yape', 'Yape')], max_length=20)),
                ('estado', models.CharField(choices=[('Pagado', 'Pagado'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.cita')),
            ],
        ),
        migrations.CreateModel(
            name='HorarioAtencion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'), ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')], max_length=10)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido_paterno', models.CharField(max_length=50)),
                ('apellido_materno', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=10)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('correo_electronico', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('contraseña', models.CharField(max_length=255)),
                ('direccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.direccion')),
            ],
        ),
        migrations.CreateModel(
            name='HistorialMedico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('diagnostico', models.CharField(max_length=50)),
                ('tratamiento', models.CharField(max_length=100)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.cita')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.paciente'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('dni', models.CharField(max_length=8, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='usuario_set', related_query_name='usuario', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='usuario_set', related_query_name='usuario', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
