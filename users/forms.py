from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label= 'Nombre de usuario')
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDITAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden")

        # Check if the email is already in use (optional, if needed)
        email = cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            self.add_error('email', "Este correo electrónico ya está en uso")

        return cleaned_data

class UserEditForm(UserChangeForm):
    
    password = None
    first_name = forms.CharField(label='Nombre', required=False)
    last_name = forms.CharField(label='Apellido', required=False)
    email = forms.EmailField(label="Email:")
    imagen = forms.ImageField(label="Avatar", required=False)
    eliminar_avatar = forms.BooleanField(required=False, initial=False, label="Eliminar Avatar")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'imagen', 'eliminar_avatar']
        # help_texts = {k:"" for k in fields}
