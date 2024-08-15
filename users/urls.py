from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views
from users.views import EditarPerfilView, ConfirmarEliminacionView


urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='Logout'),
    path('editar_perfil/', EditarPerfilView.as_view(), name='EditarPerfil'),
    path('confirmar_eliminacion/', ConfirmarEliminacionView.as_view(), name='ConfirmarEliminacion'),
    path('cambiar_pass/', views.CambiarPassView.as_view(), name='CambiarPass')
]