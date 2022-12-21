"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# ES EL FICHERO ENCARGADO DE LAS DIRECCIONES DE LA WEB
# LAS QUE ESCRIBIMOS EN LA BARRA DEL NAVEGADOR
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from contact import views as contact_views
from company import views as company_views

# aqui instanciamos la clase setting para acceder a los atributos de la misma
from django.conf import settings

# aqui le indicamos la direccion de la vista
urlpatterns = [
    path('', core_views.home, name="Inicio"),
    path('about-me/', core_views.about, name="About"),
    path('portfolio/', portfolio_views.portfolio, name="Portafolio"),
    path('contact/', contact_views.contact, name="Contacto"),
    path('company/', company_views.company, name="Coorporaciones"),
    path('admin/', admin.site.urls),
]

# Esto es una configuracion extra siempre y cuando la variable debug este true
# He importara la urls estaticas de media y lo almacena en una lista "urlpatterns"
if settings.DEBUG:
    from django.conf.urls.static import static
    # Umk,l.ñ-¨¨n nuevo patron la raiz donde son las url static que definimos en settings.py

    # De webpersonal (la raiz del proyecto)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)