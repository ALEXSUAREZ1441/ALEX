from django.db import models

# Create your models here.
class Registro(models.Model):
    name= models.CharField(max_length=50,help_text="Ingrese el nombre del estudiante")
    telephone= models.CharField(max_length=10,help_text='Ingrese el numero de telefono')
    genero= models.CharField(max_length=1,help_text='Ingrese el sexo/genero')
    date= models.DateField(auto_now=True)
    
