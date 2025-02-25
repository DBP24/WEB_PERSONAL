from django.contrib.auth.models import AbstractUser, Group
from django.db import models


from django.contrib.auth.models import BaseUserManager

class CreationUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        """
        Crea y devuelve un usuario con un correo electrónico y una contraseña.
        """
        if not email:
            raise ValueError('El usuario debe tener una dirección de correo electrónico.')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



class CreationUserModel(AbstractUser):
    # El campo cod será generado dinámicamente, no necesita un valor predeterminado fijo
    cod = models.CharField(max_length=100, blank=True, null=True, verbose_name="CODIGO")
    ruc = models.CharField(max_length=11, default="00000000000", verbose_name="RUC")
    
    # Imagen con valor predeterminado
    photo = models.ImageField(
        upload_to="static/images/", null=True, blank=True, verbose_name="foto", default="static/images/default.jpg"
    )

    # Relación con los grupos (si deseas definirla manualmente, aunque Django lo maneja por defecto)
    groups = models.ManyToManyField(
        Group, related_name='custom_user_set', blank=True, verbose_name='Groups'
    )
    
    # Relación con los permisos (si deseas definirla manualmente, aunque Django lo maneja por defecto)
    user_permissions = models.ManyToManyField(
        'auth.Permission', related_name='custom_user_permissions_set', blank=True, verbose_name='User permissions'
    )

    # Relación con un rol (definiéndolo explícitamente si lo necesitas)
    # ver bien el campo rol
    # rol = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Rol")

    # Si es necesario, define los campos que serán requeridos al crear un superusuario
    REQUIRED_FIELDS = ['email', 'ruc']
    
    # Creacion de usuario
    objects = CreationUserManager()

    def save(self, *args, **kwargs):
        if not self.cod:
            # Genera un código dinámico basado en el número de usuarios con el mismo rol
            cant_user = CreationUserModel.objects.filter(grupo=self.groups).count()
            self.cod = f'{self.groups.name} - {str(cant_user + 1).zfill(4)}'  # Esto formatea el número con ceros a la izquierda
        super().save(*args, **kwargs)
    
    

