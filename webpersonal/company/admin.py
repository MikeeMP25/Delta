from django.contrib import admin
from .models import Coorporation  # import la class of models de nuestro mismo directoy


# Register your models here.
# Extendemos la configuracion de admin.py del administrador
class CompanyAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')  # Aqui le decimos que campos de la tabla queremos que solo sea de
    # lectura no editables


# Aqui cargamos la configuracion en el sitio
admin.site.register(Coorporation, CompanyAdmin)




