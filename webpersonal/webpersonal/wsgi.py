"""
WSGI config for webpersonal project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
#ES QUE CONTIENE LA INFORMACION  PARA DESPLEJAR EL PROYECTO EN PRODUCCION 
# DESPLIEGUE 
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webpersonal.settings')

application = get_wsgi_application()
