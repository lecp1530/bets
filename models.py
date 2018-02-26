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

class Partido(models.Model):
	torneo=models.ForeignKey('Torneo',on_delete=models.PROTECT, null=True,blank=True)
	fecha_partido=models.DateField()
	equipoA=models.CharField(max_length=100)
	equipoB=models.CharField(max_length=100)
	localia=models.CharField(max_length=100)

class Polla(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=500)
	usuario=models.ForeignKey('Usuario',on_delete=models.PROTECT, null=True,blank=True)
	ganador=models.CharField(max_length=100)

class Detalle_Polla(models.Model):
	polla=models.ForeignKey('Polla',on_delete=models.PROTECT, null=True,blank=True)
	partido=models.ForeignKey('Partido',on_delete=models.PROTECT, null=True,blank=True)
	goles_equipoA=models.IntegerField()
	goles_equipoB=models.IntegerField()
	resultado=models.CharField(max_length=100)

class Bet(models.Model):
	polla=models.ForeignKey('Polla',on_delete=models.PROTECT, null=True,blank=True)
	usuario=models.ForeignKey('Usuario',on_delete=models.PROTECT, null=True,blank=True)
	pronostico_equipoA=models.CharField(max_length=100)
	pronostico_equipoB=models.CharField(max_length=100)
	puntaje=models.CharField(max_length=100)
	fecha_pronostico=models.CharField(max_length=100)







