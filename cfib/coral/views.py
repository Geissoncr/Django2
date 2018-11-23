from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Teste de tela Home.")

# Create your views here.
