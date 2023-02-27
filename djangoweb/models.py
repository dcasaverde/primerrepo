from django.db import models

# Create your models here.
class libro(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name='descripcion', null=True,max_length=250)
    
    def __str__(self):
        fila = "Nombre : " + self.nombre + "| Descripcion : " + self.descripcion
        return fila
