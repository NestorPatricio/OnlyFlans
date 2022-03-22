from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import ContactForm, Flan
from .forms import ContactFormForm


def index(request):
    public_flans = Flan.objects.filter(is_private = False)
    return render(request, './web/index.html', {'public_flans': public_flans})

def acerca(request):
    return render(request, './web/about.html', {})

def bienvenido(request):
    private_flans = Flan.objects.filter(is_private = True)
    return render(request, './web/welcome.html', {'private_flans': private_flans})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/web/')
    else:
        form = ContactFormForm()
    return render(request, './web/contact.html', {'form': form})