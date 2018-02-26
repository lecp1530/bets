from django.db import models

# Create your models here.
class Usuario(models.Model):
	username=models.CharField(max_length=50)
	nombre=models.CharField(max_length=100)
	apellidos=models.CharField(max_length=100)
	sexo=models.CharField(max_length=50)
	pais=models.CharField(max_length=50)
	email=models.EmailField()
	fecha_nacimiento=models.DateField()

class Torneo(models.Model):
	nombre=models.CharField(max_length=100)
	pais=models.CharField(max_length=100)
	año=models.IntegerField()
	flag_activo=models.IntegerField()

class Equipo(models.Model):
	nombre=models.CharField(max_length=100)
	torneo=models.ForeignKey('Torneo',on_delete=models.PROTECT, null=True,blank=True)
	pais=models.CharField(max_length=100)

class Fase(models.Model):
	nombre=models.CharField(max_length=100)

class Torneo_Fase(models.Model):
	torneo=models.ForeignKey('Torneo',on_delete=models.PROTECT, null=True,blank=True)
	fase=models.ForeignKey('Fase',on_delete=models.PROTECT, null=True,blank=True)
	fecha_partido=models.DateField()
	equipoA=models.CharField(max_length=100)
	equipoB=models.CharField(max_length=100)

class Polla(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=500)
	torneo=models.ForeignKey('Torneo',on_delete=models.PROTECT, null=True,blank=True)
	usuario=models.ForeignKey('Usuario',on_delete=models.PROTECT, null=True,blank=True)
	fase=models.ForeignKey('Fase',on_delete=models.PROTECT, null=True,blank=True)

class Bet(models.Model):
	polla=models.ForeignKey('Polla',on_delete=models.PROTECT, null=True,blank=True)
	usuario=models.ForeignKey('Usuario',on_delete=models.PROTECT, null=True,blank=True)
	equipoA=models.CharField(max_length=100)
	equipoB=models.CharField(max_length=100)
	resultadoA=models.CharField(max_length=100)
	resultadoB=models.CharField(max_length=100)







