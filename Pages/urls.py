from django.urls import path
from Pages import views

urlpatterns = [
    path('', views.home, name='home'),  # La URL base carga la vista "home"
    path('nosotros/', views.nosotros, name='nosotros'),  # Carga la vista "nosotros"
    path('staff/', views.staff, name='staff'),  # Cargar la vista "staff"
    path('especialidades/', views.especialidades, name='especialidades'),  # Carga la vista "especialidades"
    path('reservaCita/', views.loginReserva, name='loginReserva'),  # Carga la vista "reservaCita"
    path('misionVision/', views.misionVision, name='misionVision'),  # La URL base carga la vista "misionVision"
    path('historia/', views.historia, name='historia'),  # Carga la vista "historia"
    path('dashboard/', views.dashboard, name='dashboard'),  # Vista "dashboard"
    path('crearCuenta/', views.crearCuenta, name='crearCuenta'),  # Vista "crearCuenta"
]
