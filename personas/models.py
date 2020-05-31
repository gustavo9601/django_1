from django.db import models


"""
Primero se definen, las clases que no tienen relacion
"""
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio id: {self.id} | calle {self.calle} | no_calle: {self.no_calle} | pais: {self.pais}'

# Create your models here.
class Persona(models.Model):
    # se debe especificar el tipo de dato
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    # llave foranea, que se relaciona con la Clase Domicilo
    # ForeighKey(ClaseRelacion, on_delete=que hacer si se elimina un registro de ClaseRelacion, aceptaNull)

    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, null=True)

    # al ser modelo, muestra el formateo del string al listar las personasd el modelo en la consola de administracion
    def __str__(self):
        return f'Persona id: {self.id} | nombre : {self.nombre} | apellido: {self.apellido}'


