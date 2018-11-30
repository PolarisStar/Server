from django.db import models

class Perrito(models.Model):

    estados = (
        ('rescatado', 'Rescatado'),
        ('disponible', 'Disponible'),
        ('adoptado', 'Adoptado'),
    )

    imagen = models.ImageField(upload_to='perrito_image', blank=True)
    nombre = models.CharField(max_length=20)
    raza = models.CharField(max_length=30)
    descripcion= models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=estados)

class Usuario(models.Model):

    YES = '1'
    NO = '0'

    states = (
        (YES, 'Si'),
        (NO, 'No'),
    )

    username = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    admin = models.CharField(max_length=10, choices=states, default=NO)