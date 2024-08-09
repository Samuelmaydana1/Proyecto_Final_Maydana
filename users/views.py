from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from users.forms import UserRegisterForm, UserEditForm
from users.models import Avatar
import os

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('Inicio') 
    else:
        form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Login')
    else:
        form = UserRegisterForm()
    
    return render(request, "users/registro.html", {"form": form})

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST, request.FILES, instance=usuario)

        if miFormulario.is_valid():
            miFormulario.save()

            imagen = miFormulario.cleaned_data.get('imagen')
            eliminar_avatar = miFormulario.cleaned_data.get('eliminar_avatar')

            if imagen:
                avatar, creado = Avatar.objects.get_or_create(user=usuario)
                if not creado:
                    if avatar.imagen and os.path.isfile(avatar.imagen.path):
                        os.remove(avatar.imagen.path)
                avatar.imagen = imagen
                avatar.save()

            if eliminar_avatar:
                avatar = Avatar.objects.filter(user=usuario).first()
                if avatar:
                    if avatar.imagen and os.path.isfile(avatar.imagen.path):
                        os.remove(avatar.imagen.path)
                    avatar.delete()

            return redirect('EditarPerfil')

    else:
        miFormulario = UserEditForm(instance=usuario)

    avatar_actual = Avatar.objects.filter(user=usuario).first()

    return render(
        request,
        "users/editar_perfil.html",
        {
            "mi_form": miFormulario,
            "usuario": usuario,
            "avatar": avatar_actual
        }
    )

class CambiarPassView(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy('Inicio')