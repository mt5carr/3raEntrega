from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(
        request = request,
        template_name='template_base.html'
    )

def about_me(request):
    return HttpResponse("<br><h1>Ya entendí esta parte</h1>")

def saludo(request):
    return render(
        request = request,
        template_name='saludo.html'
    )