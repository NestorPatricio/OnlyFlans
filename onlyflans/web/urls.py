from django.urls import path
from .views import index, acerca, bienvenido, contacto

app_name = 'web'

urlpatterns = [
    # example: /web/
    path('', index, name = 'índice'),
    # example: /web/acerca/
    path('acerca', acerca, name = 'acerca'),
    # example: /web/bienvenido/
    path('bienvenido', bienvenido, name = 'bienvenida'),
    # example: /web/contacto/
    path('contacto', contacto, name = 'contáctanos')
]
