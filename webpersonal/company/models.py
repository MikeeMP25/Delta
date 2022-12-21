from django.db import models


# Create your models here.
class Coorporation(models.Model):

    rfc = models.IntegerField(verbose_name="RFC", primary_key=False)
    # aplica la regla de la base de datos cadena varhcar debe tener un limite de caracteres
    name_company = models.CharField(verbose_name="Nombre compañia", max_length=100, null=False)
    address = models.TextField(verbose_name="Domicilio", max_length=250)
    phone = models.CharField(verbose_name="Telefono" , max_length=10)
    e_mail = models.EmailField(verbose_name="Correo Empresarial", max_length=254, null=False)
    release_date = models.DateField(verbose_name=" Fecha de lanzamiento")
    # el atributo upload_to=le decimos donde buscar la imagen cargada y guardar lo en el directorio
    # que le asignamos "company"
    logo = models.ImageField(verbose_name="logo", upload_to="company")

    # Este se ejecuta solo una vez cuando se crea la fecha actual
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = "Compañia"  # cambiamos el nombre del encabezado de la tabla del la clase
        verbose_name_plural = "Compañias"  # Este es en plural de dos en adelante
        ordering = ["-created"]  # Es una lista de una consulta ordenada de mas resiente al mas viejo

    def __str__(self): # Metodo especial donde redefinimos el coorporation por el nombre de la compañias ya registradas
        return self.name_company

