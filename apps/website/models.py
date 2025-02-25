from django.db import models

from django.core.exceptions import ValidationError
# Adminsitrador de etiuqetas tags 
from taggit.managers import TaggableManager

class ExperienciaModel(models.Model):
    company_name = models.CharField(max_length=100) 
    url_company = models.URLField(default="") 
    rol = models.CharField(max_length=100)  
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  
    description = models.TextField(max_length=2000)
    
    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("La fecha de finalización no puede ser anterior a la de inicio.")

    def __str__(self):
        return f"{self.company_name} - {self.rol} ({self.start_date} - {self.end_date if self.end_date else 'Actualidad'})"

class StudyModel(models.Model):
    ie = models.CharField(max_length=150)
    url_company = models.URLField(default="")
    carrera = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True) 

    def clean(self):
        if self.end_date and self.end_date < self.start_date:
            raise ValidationError("La fecha de finalización no puede ser anterior a la de inicio.")
        
    def __str__(self):
        return f"{self.ie} - ({self.carrera} - {self.end_date if self.end_date else 'Actualidad'})"

class CapacityModel(models.Model):
    ie = models.CharField(max_length=150)
    tema = models.CharField(max_length=150)
    start_date = models.DateField()
    tiempo_entero = models.IntegerField(default=0)
        
    def __str__(self):
        return f"{self.ie} - ({self.tema})"

class ProjectModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    urls = models.CharField(max_length=250, verbose_name="URL Pagina Web")
    url_github = models.CharField(max_length=250, verbose_name="URL GitHub", default="")
    description = models.TextField(max_length=500, verbose_name="Descripcion")
    photo = models.ImageField(
        upload_to="static/images/", null=True, blank=True, verbose_name="foto", default="static/images/default.jpg"
    )
    #etiqueta
    tags = TaggableManager()
