from django.shortcuts import render
from django.http import HttpResponse
from APP.models import Modo_de_juego, last_update,nickname

from django.template import loader
# Create your views here



def start(request):
    return render(request, "APP/index.html")

def modo_de_juego(request):

    return render(request,"APP/modo.html")

def last_update(request):

    return render(request,"APP/updates.html")

def nickname(request):

    return render(request,"APP/players.html")
