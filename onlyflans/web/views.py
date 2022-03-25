from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import ContactForm, Flan
from .forms import ContactFormForm, ContactFormModelForm, UserRegisterForm


def index(request):
    public_flans = Flan.objects.filter(is_private = False)
    return render(request, './web/index.html', {'public_flans': public_flans})

def acerca(request):
    return render(request, './web/about.html', {})

@login_required
def bienvenido(request):
    private_flans = Flan.objects.filter(is_private = True)
    return render(request, './web/welcome.html', {'private_flans': private_flans})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/web/exito')
    else:
        form = ContactFormModelForm()
    return render(request, './web/contact.html', {'form': form})

def exito(request):
    return render(request, './web/success.html', {})

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            contrasena = form.cleaned_data['password1']
            new_user = authenticate(username = usuario, password = contrasena)
            login(request, user = new_user)
            messages.success(request, f'Usuario {usuario} registrado exitosamente.')
            return redirect('/web/')
    else:
        form = UserRegisterForm()
    return render(request, './web/register.html', {'form': form})

def buscaflanes(request):
    if request.method == 'POST':
        # 'buscador' guarda el valor ingresado en el formulario de búsqueda.
        buscador = request.POST['buscador']
        # Filtrar los distintos objetos flanes para que coincidan con nuestro
        # criterio de búsqueda. En este caso, con el nombre de cada flan.
        flanes = Flan.objects.filter(name__contains = buscador)
        return render(request, './web/results_flans.html', {
            'buscador': buscador,
            'flanes': flanes,
            })
        
    else:
        return render(request, './web/results_flans.html', {})
    
    