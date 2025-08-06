from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def criar_usuario(request):
    #return HttpResponse("<hi> Alô senai Games! </hi>")
    #request - requisição
    #tamplate - html, entre outros front end
    #context - objetos, python com banco de dados
    return render(request, 'crud_base/usuario_lead.html')