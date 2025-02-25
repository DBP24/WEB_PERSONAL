from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ExperienciaModel,CapacityModel,StudyModel,ProjectModel
class Index(TemplateView):
    template_name ='website/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Diego Bonatti'
        context['profile'] = 'Soy Ingeniero de Sistemas con experiencia en desarrollo web, creación de aplicaciones personalizadas y diseño de APIs RESTful. Manejo tecnologías como Python, PHP, Django, JavaScript, Power BI y MySQL. Me especializo en la optimización de procesos mediante metodologías ágiles como Scrum, combinando habilidades técnicas y gestión de proyectos para mejorar la experiencia del usuario y la eficiencia operativa.'
        context['download'] ='Si deseas conocerme más, te invito a descargar mi currículum actualizado. '
        return context

class Curriculum(TemplateView):
    template_name = 'website/curriculum.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['experiencias'] = ExperienciaModel.objects.all()
        context['capacitaciones'] = CapacityModel.objects.all().order_by('-start_date')
        context['estudios'] = StudyModel.objects.all()
        return context


from django.core.paginator import Paginator
from datetime import datetime
class Projects(TemplateView):
    template_name = 'website/proyect.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = ProjectModel.objects.all()
        context['year'] = datetime.now().year
        return  context