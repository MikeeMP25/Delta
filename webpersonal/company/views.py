from django.shortcuts import render
from .models import Coorporation  # Aqui importamos los modelos de la base de datos de la tabla coorporation


# Create your views here.
def company(request):
    # El objeto objects con su metodo all es crea e inicializa una vez cargado el proyecto runserver
    # donde almacenamos todos los registros actuales de la tabla company es una consulta
    coorporations = Coorporation.objects.all()
    # retornamos una redirecion carpeta company/company.html y le mandamos un objeto con la lista de registros actuales
    return render(request, "company/company.html", {'organizaciones': coorporations})