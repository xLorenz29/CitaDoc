from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import Paciente
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login as auth_login

# Create your views here.

def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def staff(request):
    return render(request, 'staff.html')

def especialidades(request):
    return render(request, 'especialidades.html')


def misionVision(request):
    return render(request, 'misionVision.html')

def historia(request):
    return render(request, 'historia.html')


def dashboard(request):
    return render(request, 'dashboard.html')

def loginReserva(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            numero_documento = form.cleaned_data['numero_documento']
            contraseña = form.cleaned_data['contraseña']
            
            try:
                paciente = Paciente.objects.get(dni=numero_documento)
                
                # Caso 1: Contraseña hasheada
                if paciente.contraseña.startswith('pbkdf2_sha256$'):
                    if check_password(contraseña, paciente.contraseña):
                        request.session['paciente_id'] = paciente.id
                        return redirect('dashboard')
                
                # Caso 2: Contraseña en texto plano (solo durante transición)
                elif contraseña == paciente.contraseña:
                    # Hasheamos la contraseña para futuros logins
                    paciente.contraseña = make_password(contraseña)
                    paciente.save()
                    request.session['paciente_id'] = paciente.id
                    return redirect('dashboard')
                
                return HttpResponse("Credenciales incorrectas")
                    
            except Paciente.DoesNotExist:
                return HttpResponse("Paciente no encontrado")
    
    else:
        form = LoginForm()
    return render(request, 'loginReserva.html', {'form': form})


'''def loginReserva(request):
    if request.method == 'POST':
        
        #Creo el formulario de autenticación
        form = AuthenticationForm(request, data=request.POST)
        
        #Verifico si los datos ingresados cumplen mi formato
        if form.is_valid():
            dni = form.cleaned_data.get('username')  # Sería el número de documento
            password = form.cleaned_data.get('password')
    
            #Autentico al usuario con el dni y la contraseña -> devuelve el usuario si es correcto
            user = authenticate(request, username=dni, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return HttpResponse("Credenciales inválidas")
        
        #Si los datos ingresados no cumple con el formato
        else:
            return HttpResponse("Formulario inválido")
    
    #Si mi solicitud es Get, solo muestro el formulario de autenticación
    else:
        form = AuthenticationForm()
    
    return render(request, 'loginReserva.html', {'form': form})'''



def nuevologin(request):
    
    return render(request, 'nuevologin.html')
    