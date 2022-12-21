from django.contrib import admin
from .models import Personal  # import la clase personal de modelos de contacto


# Register your models here.

class PersonalAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


# Son los modelos controlador de vistas del superusuario(Admin)

admin.site.register(Personal, PersonalAdmin)
