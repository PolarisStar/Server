from django.db import models

class Perrito(models.Model):
    nombrePerro = models.CharField(max_length=50)
    razaP = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen =  models.FileField(max_length=None, upload_to='media')
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombrePerro + ' - ' + self.razaP + ' - ' + self.descripcion + ' - ' + self.estado