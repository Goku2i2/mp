from django.db import models
from django.utils import timezone

#Permisos DJANGO 
from django.utils.translation import ugettext as _

ESTADOS= (
    ('Rescatado', 'Rescatado'),
    ('Disponible', 'Disponible'),
    ('Adoptado', 'Adoptado'),
)

class Perros_Rescatados(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    estado= models.CharField(max_length=30, choices=ESTADOS, default='')
    #Subir archivos
    fotografia_perro=models.FileField(blank=True, null=True)
    nombre_perro = models.CharField(max_length=200)
    raza_predominante = models.CharField(max_length=200)
    descripcion=models.TextField()
    #Lista de estados 
    # created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre_perro

    class Meta:
        permissions = (
            ('adoptantes', _('Adoptantes')),
        )  
