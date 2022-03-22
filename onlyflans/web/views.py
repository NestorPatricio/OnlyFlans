from django.shortcuts import render
from .models import Flan


def index(request):
    public_flans = Flan.objects.filter(is_private = False)
    return render(request, './web/index.html', {'flans': public_flans})

def acerca(request):
    return render(request, './web/about.html', {})

def bienvenido(request):
    private_flans = Flan.objects.filter(is_private = True)
    return render(request, './web/welcome.html', {'flans': private_flans})

def contacto(request):
    return render(request, './web/contact.html', {})