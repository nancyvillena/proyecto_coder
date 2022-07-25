from django.db import models

# Create your models here.
class Film(models.Model):
       name = models.CharField(max_length=255)
       sinopsis = models.CharField(max_length=255)
       duration = models.TimeField()
       poster = models.ImageField(upload_to="films", null=True)
       
       def __str__(self):
          return f"ID- ID: {self.id} - Nombre: {self.name} - Sinopsis: {self.sinopsis} - Duration: {self.duration} - poster{self.poster}"
       
class Custumer(models.Model):
      name = models.CharField(max_length=255)
      asiento = models.CharField(max_length=255)
      email = models.EmailField()
      
class Funciones(models.Model):
      sala = models.CharField(max_length=255)
      horario = models.DateTimeField("Horario")
      film = models.ForeignKey(Film , on_delete=models.CASCADE) 
       