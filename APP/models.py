from django.db import models

# Create your models here.
class Modo_de_juego(models.Model):
    modo=models.CharField(max_length=30)

class nickname(models.Model):
    nick=models.CharField(max_length=10)
    Sc0re=models.IntegerField()

class last_update(models.Model):
    Fecha=models.DateField()
    