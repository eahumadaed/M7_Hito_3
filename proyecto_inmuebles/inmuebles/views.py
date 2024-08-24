from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

from .services import crear_usuario, obtener_usuario, actualizar_usuario, eliminar_usuario
from .forms import UsuarioForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios/list.html', {'usuarios': usuarios})

def usuario_detail(request, id):
    try:
        usuario = obtener_usuario(id)
    except Usuario.DoesNotExist:
        raise Http404("Usuario no encontrado")
    return render(request, 'usuarios/detail.html', {'usuario': usuario})

def usuario_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            crear_usuario(form.cleaned_data)
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('usuario_list')
    else:
        form = UsuarioForm()
    return render(request, 'usuarios/form.html', {'form': form})

def usuario_update(request, id):
    usuario = obtener_usuario(id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            actualizar_usuario(id, form.cleaned_data)
            return redirect('usuario_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuarios/form.html', {'form': form})

def usuario_delete(request, id):
    eliminar_usuario(id)
    return redirect('usuario_list')


def index(request):
    return render(request, 'index.html')