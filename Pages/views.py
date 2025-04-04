from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Paciente
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import login as auth_login
# Create your views here.

def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'Fnosotros/nosotros.html')

def misionVision(request):
    return render(request, 'Fnosotros/misionVision.html')

def historia(request):
    return render(request, 'Fnosotros/historia.html')

def staff(request):
    return render(request, 'Fstaff/staff.html')

def especialidades(request):
    return render(request, 'Fespecialidades/especialidades.html')


def dashboard(request):
    # Dado que para ingresar a esta vista, el usuario ya tiene que haber iniciado sesión,
    paciente_id = request.session.get('paciente_id')  # Obtenemos el id del paciente

    if not paciente_id:
        return redirect('loginReserva')  # En caso no haya sesión, lo mandamos al login
    
    # Pero si hay sesion, obtenemos el paciente activo
    PacienteActivo = Paciente.objects.get(id=paciente_id)
    
    return render(request, 'dashboard.html', {'PacienteActivo': PacienteActivo})

def loginReserva(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            numero_documento = form.cleaned_data['numero_documento']
            contraseña = form.cleaned_data['contraseña']
            
            try:
                paciente = Paciente.objects.get(dni=numero_documento)
                
                # Verificamos si la contraseña está hasheada o en texto plano
                if paciente.contraseña.startswith('pbkdf2_sha256$'):
                    # Si está hasheada, validamos que exista en la BD con check_password
                    if check_password(contraseña, paciente.contraseña):
                        request.session['paciente_id'] = paciente.id
                        return redirect('dashboard')
                    else:
                        messages.error(request, "Credenciales incorrectas")
                        return redirect('loginReserva')
                
                elif contraseña == paciente.contraseña:
                    # Si está en texto plano, la hashamos y guardamos
                    paciente.contraseña = make_password(contraseña)
                    paciente.save()
                    request.session['paciente_id'] = paciente.id
                    return redirect('dashboard')
                else:
                    messages.error(request, "Credenciales incorrectas")
                    return redirect('loginReserva')
            except Paciente.DoesNotExist:
                messages.error(request, "El número de documento no existe")
                return redirect('loginReserva')
    
    else:
        form = LoginForm()

    return render(request, 'loginReserva.html', {'form': form})

def crearCuenta(request):
    return render(request, 'crearCuenta.html')

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
