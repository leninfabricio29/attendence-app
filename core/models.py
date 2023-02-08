from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=15)
    imageProfile = models.ImageField(null=True, blank=True, upload_to="images/profile")
    departamento = models.CharField(max_length=20)
    fechaIngreso = models.DateField(null=True)
    estado = models.BooleanField(default=False)
    direcion = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)


class Attendence (models.Model):
    attendenceProfile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    fecha = models.DateField(null=True)
    turno = models.CharField(max_length=5, null=True)
    horaInicio = models.TimeField(null=True)
    horaFin = models.TimeField(null=True)
    totalHoras = models.CharField(max_length=2)

    def __str__(self):
        return str(self.fecha)





