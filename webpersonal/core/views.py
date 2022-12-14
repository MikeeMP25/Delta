from django.shortcuts import render, HttpResponse

# Create your views here.
#aqui estan la vistas para el usuario 

#variable html 
html_base="""
<h1>Mi blog personal</h1>
<ul>
     <li><a href="/">Inicio</a></li>
     <li><a href="/about/">Acerca de</a></li>
</ul>
"""

#vamos a definir una vista como si fuera una funcion recibe como parametros un request
# RETORNA COMO RESPUESTA UN OBJETO HTTPRESPONSE  
def home(request):
    html_respose="<h1>Inicio</h1><p>Bienvenidos</p><br> <ul>"
    for l in range(1,11):
        html_respose+="<li>Proyecto Caja #{}</li>".format(l)
    html_respose+="</ul>"    
    return HttpResponse(html_base+html_respose)

def about(request):
    return HttpResponse(html_base+"""<h1>Acerca de</h1>
    <h2>Ing. Jesús Miguel Miranda Pérez</h2><br>
    <p>Desarrollador (babyJunior)</p><br>
    <p>Coorporación MADD SYSTEM GROUP</p>""")