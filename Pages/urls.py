from django.urls import path
from Pages import views

urlpatterns = [
    path('home/', views.home, name='home'),  # La URL base carga la vista "home"
    path('nosotros/', views.nosotros, name='nosotros'),  # La URL base carga la vista "nosotros"
    path('staff/', views.staff, name='staff'),  # La URL base carga la vista "staff"
    path('especialidades/', views.especialidades, name='especialidades'),  # La URL base carga la vista "especialidades"
    path('reservaCita/', views.loginReserva, name='loginReserva'),  # La URL base carga la vista "reservaCita"
    path('misionVision/', views.misionVision, name='misionVision'),  # La URL base carga la vista "misionVision"
    path('historia/', views.historia, name='historia'),  # La URL base carga la vista "historia"
    path('dashboard/', views.dashboard, name='dashboard'),  # La URL base carga la vista "dashboard"
    path('nuevologin/', views.nuevologin, name='nuevoLogin'), 
]
