from django.shortcuts import render, HttpResponse

# Create your views here.
# aqui estan la vistas para el usuario


# vamos a definir una vista como si fuera una funcion recibe como parametros un request
# RETORNA COMO RESPUESTA UN OBJETO HTTPRESPONSE  
def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def portfolio(request):
    return render(request, "core/portfolio.html")


def contact(request):
    return render(request, "core/contact.html")
