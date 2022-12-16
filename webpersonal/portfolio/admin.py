from django.contrib import admin
from .models import Project
# from . hace referencia al mismo directorio models.py

#extender las funciones del admin
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Project,ProjectAdmin)

# Register your models here.

#agregamos el panel del proyect de los modelos de mi tabla
