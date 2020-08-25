from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    slug = models.SlugField(max_length=50)
    created_at = models.DateTimeField(auto_now=True) #dame la fecha cuando se crea el registro

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'  # Nombre que lleva cuando registre mi aplicación en el modulo de administración de django
        verbose_name_plural = 'Videos'
        db_table = 'video'  # nombre de la tabla
        ordering = ['id']  # ordena por id de forma ascendente, si queremos que sea descendente [-id]

