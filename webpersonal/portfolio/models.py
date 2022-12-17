from django.db import models


# Create your models here.

#   EL MODELO JUEGA DIRECTAMENTE CON LA VISTA DEL USUARIO ADMIN

# Creamos la clase que nos servira como modelo para nuestra tabla de base de datos
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    # aplica la regla de la base de datos cadena varhcar debe tener un limite de caracteres
    image = models.ImageField(verbose_name="Imagen", upload_to="projects")
    # Este se ejecuta solo una vez cuando se crea la fecha actual
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    description = models.TextField(verbose_name="Descripción")

    # Este obtiene la fecha de cuando se actualizo este registro

    # Configuracion del idioma a español
    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    # Nos devuelve el nombre del proyecto
    def __str__(self):
        return self.title
