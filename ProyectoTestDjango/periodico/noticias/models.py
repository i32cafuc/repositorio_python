from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)  
 
class Seccion(models.Model):
    nombre = models.CharField(max_length = 255)
    categoria = models.CharField(max_length = 255)
 
class Noticia(models.Model):
    titulo = models.CharField(max_length = 255)
    descripcion = models.TextField()
    autor = models.ForeignKey(Autor)
    seccion = models.ForeignKey(Seccion)
