from django.db import models


# Create your models here.
class Personal(models.Model):
    id_personal = models.IntegerField(verbose_name="No_registro", primary_key=True)
    # aplica la regla de la base de datos cadena varhcar debe tener un limite de caracteres
    name_complet = models.TextField(verbose_name="Nombre completo", max_length=100, null=False)
    adreess = models.TextField(verbose_name="Domicilio", max_length=250)
    cellphont = models.IntegerField(verbose_name="Celular")
    e_mail = models.EmailField(verbose_name="Correo Electronico", max_length=254, null=False)
    date_of_birth = models.DateTimeField(verbose_name=" Fecha de Nacimiento")
    # el atributo upload_to=le decimos donde buscar la imaneg o guardarlo
    photo = models.ImageField(verbose_name="Foto", upload_to="foto")

    # Este se ejecuta solo una vez cuando se crea la fecha actual
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    # Este obtiene la fecha de cuando se actualizo este registro

    # Configuracion del idioma a español
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Pelfiles"
        ordering = ["-created"]

    # Nos devuelve el nombre del del registro de la base de datos

    def __str__(self):
        print(self.name_complet)
        return self.name_complet
