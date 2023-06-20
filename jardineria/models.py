from django.db import models

# Create your models here.

class Categoria(models.Model):
    codigo_cat = models.IntegerField(primary_key=True, verbose_name="Id de la categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de categoria")

    def str(self):
        return self.nombreCategoria

class Jardineria(models.Model):
    codigo = models.IntegerField(primary_key=True, verbose_name="Codigo de barra")
    Nombre= models.CharField(max_length=50, blank=True, verbose_name="Nombre Producto")
    categoria= models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    tipo = models.CharField(max_length=30, blank=True, verbose_name="Tipo de producto")
    imagen = models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    
    
    def str(self):
        return self.codigo
    