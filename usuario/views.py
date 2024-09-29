from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistroUsuarioForm, LoginForm, AzucarForm, GlutenFreeForm, VeganoForm, Azucar, GlutenFree, Vegano
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q



# views.py
from django.shortcuts import render, redirect
from .forms import VeganoForm, AzucarForm,GlutenFreeForm


# Vista de registro
def register_view(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Autenticar y loguear al usuario después de registrarse (opcional)
            login(request, user)
            messages.success(request, 'Registro exitoso. Bienvenido, ¡has iniciado sesión!')
            return redirect('home')  # Redirigir al home o donde desees
        else:
            messages.error(request, 'Hubo un error en el registro, revisa los datos.')
    else:
        form = RegistroUsuarioForm()
    
    return render(request, 'register.html', {'form': form})

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menu_principal')  # Redirige al menú principal tras iniciar sesión
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Vista para cerrar sesión
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')  # Redirigir al login después de cerrar sesión

# Vista para la página principal (home)
def home(request):
    return render(request, 'home.html')  # Asegúrate de que tienes un template llamado home.html



# Vista del menú principal con búsqueda
def menu_principal(request):
    query = request.GET.get('q')  # Obtener el término de búsqueda desde el formulario
    resultados = []

    if query:
        # Buscar en el campo 'nombre_producto' de cada modelo
        resultados_azucar = Azucar.objects.filter(Q(nombre_producto__icontains=query))
        resultados_vegano = Vegano.objects.filter(Q(nombre_producto__icontains=query))
        resultados_gluten = GlutenFree.objects.filter(Q(nombre_producto__icontains=query))

        # Unir los resultados en una lista
        resultados = list(resultados_azucar) + list(resultados_vegano) + list(resultados_gluten)

    context = {
        'resultados': resultados,  # Pasamos los resultados al template
    }

    return render(request, 'menu_principal.html', context)


# Vista para ingresar productos
def ingresar_azucar(request):
    if request.method == 'POST':
        form = AzucarForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el producto la bbdd
            return redirect('menu_principal')  # Redirige al menú principal después de guardar
    else:
        form = AzucarForm()

    return render(request, 'ingresar_azucar.html', {'form': form})



def ingresar_vegano(request):
    if request.method == 'POST':
        form = VeganoForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el producto la bbdd
            return redirect('menu_principal')  # Redirige al menú principal después de guardar
    else:
        form = VeganoForm()

    return render(request, 'ingresar_vegano.html', {'form': form})

def ingresar_gluten(request):
    if request.method == 'POST':
        form = GlutenFreeForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el producto la bbdd
            return redirect('menu_principal')  # Redirige al menú principal después de guardar
    else:
        form = GlutenFreeForm()

    return render(request, 'ingresar_gluten.html', {'form': form})


def about(request):
    return render(request, 'about.html')




