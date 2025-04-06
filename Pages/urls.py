from django.urls import path
from Pages import views

urlpatterns = [
    path('', views.home, name='home'),  # La URL base carga la vista "home"
    path('nosotros/', views.nosotros, name='nosotros'),  # Carga la vista "nosotros"
    path('staff/', views.staff, name='staff'),  # Cargar la vista "staff"
    path('especialidades/', views.especialidades, name='especialidades'),  # Carga la vista "especialidades"
    path('reservaCita/', views.loginReserva, name='loginReserva'),  # Carga la vista "reservaCita"
    path('logout/', views.logout, name='logout'),  # Carga la vista "logout"
    path('misionVision/', views.misionVision, name='misionVision'),  # La URL base carga la vista "misionVision"
    path('historia/', views.historia, name='historia'),  # Carga la vista "historia"
    path('crearCuenta/', views.crearCuenta, name='crearCuenta'),  # Vista "crearCuenta"
    path('dashboard1', views.dashboard1, name='dashboard1'),  # Vista "dashboard"
    path('dashboard2', views.dashboard2, name='dashboard2'),  # Vista "dashboard"
    path('dashboard3', views.dashboard3, name='dashboard3'),  # Vista "dashboard"
    path('dashboard4', views.dashboard4, name='dashboard4'),  # Vista "dashboard"
]
