from django.shortcuts import render
from .models import Project


# Create your views here.
# AQUI RENDERIZAMOS A LA VISTA PORTFOLIO.HTML
def portfolio(request):
    # Una lista de los proyectos creados en la base de datos
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html", {'project': projects})
