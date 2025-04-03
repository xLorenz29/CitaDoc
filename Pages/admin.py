from django.contrib import admin
from .models import Direccion, Doctor, Paciente, HorarioAtencion, Cita, HistorialMedico, Factura
from django.contrib.sessions.models import Session

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Direccion)
admin.site.register(Paciente)
admin.site.register(HorarioAtencion)
admin.site.register(Cita)
admin.site.register(HistorialMedico)
admin.site.register(Factura)
admin.site.register(Session)
