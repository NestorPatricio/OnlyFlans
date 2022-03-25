from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import index, acerca, bienvenido, contacto, exito, registro, buscaflanes

app_name = 'web'

urlpatterns = [
    # example: /web/
    path('', index, name = 'índice'),
    # example: /web/acerca/
    path('acerca', acerca, name = 'acerca'),
    # example: /web/bienvenido/
    path('bienvenido', bienvenido, name = 'bienvenida'),
    # example: /web/contacto/
    path('contacto', contacto, name = 'contáctanos'),
    # example: /web/exito/
    path('exito', exito, name = 'éxito'),
    # example: /web/registro/
    path('registrar', registro, name = 'regístrate'),
    # example: /web/accounts/login/
    path('accounts/login', auth_views.LoginView.as_view(template_name = 'web/registration/login.html'), name = 'login'),
    # example: /web/accounts/logout/
    path('accounts/logout', auth_views.LogoutView.as_view(template_name = 'web/registration/logged_out.html'), name = 'logout'),
    # example: /web/buscaflan/
    path('buscaflan', buscaflanes, name = 'búscalo')
]
