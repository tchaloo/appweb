from django.shortcuts import render

# Create your views here.

#-*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime

def home(request):
    text="""<h1>Bienvenue sur mon blog!!!</h1>
    <p>Vous verrez qu'il est super cool</p>"""
    return HttpResponse(text)

def fonctiontpl(request):
    return render(request, 'exo/tpl.html', {'current_date':
    datetime.now()})

def fonctionessai(request):
    return render(request, 'exo/page1.html')

def fonctionadd(request, nombre1, nombre2):
    nombre1=12
    nombre2=24
    total = int(nombre1) + int(nombre2)
    return render(request, 'exo/addition.html', locals())

from exo.forms import Formulaire
def fonctionform(request):
    if request.method == 'POST':
        form = Formulaire(request.POST)
        if form.is_valid():
            sujet = form.cleaned_data['sujet']
            message = form.cleaned_data['message']
            envoyeur = form.cleaned_data['envoyeur']
            renvoi = form.cleaned_data['renvoi']

            envoi = True
    else:
        form = Formulaire()
    return render(request, 'exo/formulaire.html', locals())
