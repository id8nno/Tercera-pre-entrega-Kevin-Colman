from django.shortcuts import render
from django.http import HttpResponse
from APP.models import Modo_de_juego
# Create your views here.
def start(request):
    return HttpResponse("BIENVENIDOS")

def modo_de_juego(request):

    return HttpResponse("MODOS DE JUEGO WOW")

def last_update(request):

    return HttpResponse("ULTIMA UPDATE WOW")

def nickname(request):

    return HttpResponse("ALTO NICKNAME WOW")
