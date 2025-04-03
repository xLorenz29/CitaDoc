from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

class Direccion(models.Model):
    pais = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    distrito = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.distrito}, {self.provincia}, {self.departamento}, {self.pais}"

class Doctor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=30)
    telefono = models.PositiveIntegerField(null=True, blank=True)
    numero_colegiado = models.CharField(max_length=20, unique=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} ({self.especialidad})"

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    dni = models.CharField(max_length=8, unique=True)
    fecha_nacimiento = models.DateField()
    SEXO_CHOICES = [('Masculino', 'Masculino'), ('Femenino', 'Femenino')]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    correo_electronico = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    contraseña = models.CharField(max_length=255)  # Añadido para la contraseña

    def set_contraseña(self, password):
        """Método para establecer la contraseña de forma segura."""
        self.contraseña = make_password(password)

    def check_contraseña(self, password):
        """Método para verificar la contraseña de forma segura."""
        return check_password(password, self.contraseña)

    def __str__(self):
        return f"{self.nombre} {self.apellido_paterno} {self.apellido_materno}"


class HorarioAtencion(models.Model):
    DIAS_SEMANA = [
        ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo')
    ]
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.doctor} - {self.dia_semana} ({self.hora_inicio} - {self.hora_fin})"

class Cita(models.Model):
    fecha_hora = models.DateTimeField()
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Completado', 'Completado')
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')
    motivo_consulta = models.CharField(max_length=100, null=True, blank=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cita con {self.doctor} - {self.paciente} ({self.fecha_hora})"

class HistorialMedico(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    diagnostico = models.CharField(max_length=50)
    tratamiento = models.CharField(max_length=100)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)

    def __str__(self):
        return f"Historial de {self.paciente} - {self.fecha_registro}"

class Factura(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    METODO_PAGO_CHOICES = [
        ('Tarjeta', 'Tarjeta'),
        ('Efectivo', 'Efectivo'),
        ('Yape', 'Yape')
    ]
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)
    ESTADO_CHOICES = [
        ('Pagado', 'Pagado'),
        ('Pendiente', 'Pendiente')
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='Pendiente')

    def __str__(self):
        return f"Factura {self.id} - {self.estado}"
