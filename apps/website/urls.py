from django.urls import path
from .views import Index,Curriculum,Projects,PrivacyPolicy
urlpatterns = [
    path("", Index.as_view(), name="sobre_mi"),
    path("curriculum", Curriculum.as_view(), name="curriculum"),
    path("proyectos", Projects.as_view(), name="projects"),
    path("politica_de_privacidad", PrivacyPolicy.as_view(), name="privacyPolicy"),
  
]
