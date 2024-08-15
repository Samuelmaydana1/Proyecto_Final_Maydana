from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='Login'),
    path('register/', views.RegisterView.as_view(), name='Register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='Logout'),
    path('editar_perfil/', views.EditarPerfilView.as_view(), name='EditarPerfil'),
    path('confirmar_eliminacion/', views.ConfirmarEliminacionView.as_view(), name='ConfirmarEliminacion'),
    path('cambiar_pass/', views.CambiarPassView.as_view(), name='CambiarPass')
]