from django.db import models

# Create your models here.
class Categoria(models.Model):
    name = models.CharField(
        help_text="Nome da Categoria",
        unique=True,
        max_length=80,
    )
    description= models.TextField(
        null=True,
        blank=True,
    )
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.name = self.name.upper()
        
        super(Categoria,self).save(*args,**kwargs)
