from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import RegisterSuperAdminView,DashboardView ,CustomLoginview ,RegisterUserView

urlpatterns = [
    path("", CustomLoginview.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("registro-usuario-super-administrador", RegisterSuperAdminView.as_view(), name="register_superadmin"),

    # Dashboard
    path("dashboard",DashboardView.as_view(), name="dashboard"),
    path("registro-usuario",RegisterUserView.as_view(), name="register_user"),
]
