from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
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

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/editar_perfil.html'
    success_url = reverse_lazy('EditarPerfil')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)

        imagen = form.cleaned_data.get('imagen')
        eliminar_avatar = form.cleaned_data.get('eliminar_avatar')

        if imagen:
            avatar, creado = Avatar.objects.get_or_create(user=self.request.user)
            if not creado:
                if avatar.imagen and os.path.isfile(avatar.imagen.path):
                    os.remove(avatar.imagen.path)
            avatar.imagen = imagen
            avatar.save()

        if eliminar_avatar:
            avatar = Avatar.objects.filter(user=self.request.user).first()
            if avatar:
                if avatar.imagen and os.path.isfile(avatar.imagen.path):
                    os.remove(avatar.imagen.path)
                avatar.delete()

        return response

class ConfirmarEliminacionView(LoginRequiredMixin, View):
    template_name = 'users/confirmar_eliminacion.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        usuario = request.user

        avatar = Avatar.objects.filter(user=usuario).first()
        if avatar:
            if avatar.imagen and os.path.isfile(avatar.imagen.path):
                os.remove(avatar.imagen.path)
            avatar.delete()

        usuario.delete()

        return HttpResponseRedirect(reverse('Inicio'))

class CambiarPassView(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy('Inicio')