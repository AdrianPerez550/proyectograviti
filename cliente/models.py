from django.db import models


from django.db import models
class Cliente(models.Model):
    id=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre',default='')
    apelidopate=models.CharField(max_length=100,verbose_name='Apellido_paterno', default='')
    apelidomater=models.CharField(max_length=100,verbose_name='Apellidom', default='')
    edad =models.CharField(max_length=100,verbose_name='edad', default='')
    
    
    def __str__(self):
        fila = "Nombre:"+self.nombre+"-"+"Apellido:"+self.apelidopate
        return fila
# Create your models here.
