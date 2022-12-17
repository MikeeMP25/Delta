from django.shortcuts import render, HttpResponse

# Create your views here.
# aqui estan la vistas para el usuario


# vamos a definir una vista como si fuera una funcion recibe como parametros un request

# RETORNA COMO RESPUESTA UN OBJETO HTTPRESPONSE
#VISTA DE INICIO
def home(request):
    return render(request, "core/home.html")


# VISTA DE ACERCA DE
def about(request):
    return render(request, "core/about.html")

#VISTA DE CONTACTO RETORNA REDIRECCION DEL CONTACT.HTML LA PAGINA WEB
def contact(request):
    return render(request, "core/contact.html")
