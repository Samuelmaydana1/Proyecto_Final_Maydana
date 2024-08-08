from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views


urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='Logout'),
    path('editar_perfil/', views.editar_perfil, name='EditarPerfil'),
    path('cambiar_pass/', views.CambiarPassView.as_view(), name='CambiarPass')
]