from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from users.forms import UserRegisterForm, UserEditForm
from users.models import Avatar
import os

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return redirect('Inicio')
        
        return render(request, "users/login.html", {"form": form})

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "users/registro.html", {"form": form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('Login')
        
        return render(request, "users/registro.html", {"form": form})

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'users/editar_perfil.html'
    success_url = reverse_lazy('EditarPerfil')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        return context

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
    def get(self, request, *args, **kwargs):
        return render(request, 'users/confirmar_eliminacion.html')

    def post(self, request, *args, **kwargs):
        password = request.POST.get('password')

        # Verificar la contraseña
        if request.user.check_password(password):
            user = request.user
            
            try:
                avatar = Avatar.objects.get(user=user)
                if avatar.imagen and os.path.isfile(avatar.imagen.path):
                    os.remove(avatar.imagen.path)
                avatar.delete()
            except Avatar.DoesNotExist:
                pass
            
            user.delete()
            return redirect('Register')
        else:
            messages.error(request, "La contraseña ingresada es incorrecta. Intenta de nuevo.")
            return render(request, 'users/confirmar_eliminacion.html')

class CambiarPassView(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/cambiar_pass.html"
    success_url = reverse_lazy('Inicio')