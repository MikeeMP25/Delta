from django.shortcuts import render
from .models import Personal


# Create your views here.
# VISTA DE CONTACTO RETORNA REDIRECCION DEL CONTACT.HTML LA PAGINA WEB

def contact(request):
    # Una lista de los proyectos creados en la base de datos
    people = Personal.objects.all()
    return render(request, "contact/contact.html", {'personas': people})
# Create your views here.

