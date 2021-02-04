from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.


class Tache(models.Model):
    owner = models.ForeignKey(User, related_name='Tache_oner', on_delete=models.CASCADE)
    titre = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    date_creation = models.DateTimeField(auto_now=True)
    date_tache = models.DateTimeField(verbose_name='Date de tâche', blank=True)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    type_de_tache = models.ForeignKey("TypeDeTache",verbose_name='Type', on_delete=models.DO_NOTHING, null=True)
    

    def __str__(self):
        return self.titre




class Category(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class TypeDeTache(models.Model):
    tp = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.tp)
        super(TypeDeTache,self).save(*args, **kwargs)

    def __str__(self):
        return self.tp