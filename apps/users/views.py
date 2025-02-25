from django.shortcuts import redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomUserSuperAdminCreationForm, CreationUserForm

# login
class CustomLoginview(LoginView):
    template_name = 'users/login.html'
    def get(self, request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().get(request,*arg, **kwargs)

    
# register
class RegisterSuperAdminView(LoginRequiredMixin,generic.CreateView):
    form_class = CustomUserSuperAdminCreationForm
    template_name = 'users/register_user_super_admin.html'
    success_url = reverse_lazy('dashboard')

    def from_valid(self,form):
        user = form.save()
        user.is_active = True
        user.save()

        return super().form_valid(form)

class RegisterUserView(LoginRequiredMixin,generic.CreateView):
    form_class = CreationUserForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('dashboard')
    # sobreescribir en metodo para enviar al usuario
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()  # Obtenemos los parámetros del formulario por defecto
        kwargs['user'] = self.request.user  # Añadimos el usuario logueado al kwargs
        return kwargs
    
    def from_valid(self,form):
        user = form.save()
        user.save()
        return super().form_valid(form)

# dashboard
class DashboardView(LoginRequiredMixin,generic.ListView):
    model = User
    template_name = 'users/dashboard.html'
    context_object_name = "users"
