# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group
from .models import CreationUserModel

class CustomUserSuperAdminCreationForm(UserCreationForm):
    # si se desea agregar campos adicionales
    # ruc = forms.CharField(max_length=11,label='Ruc')
    # meta
    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name',
                  'is_staff','is_superuser', 
                  'password1', 'password2', 'is_active','groups')
        # fields = ('__all__')

        '''
        is_staff is_superuser groups
        '''

class CreationUserForm(UserCreationForm):
    class Meta:
        model = CreationUserModel
        fields = ('username','email','first_name', 'last_name',
                  'is_staff','is_superuser', 
                  'password1', 'password2','groups','ruc', 'photo',)
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user',None)
        super().__init__(*args, **kwargs)
        print(user)
        if user and user.is_superuser:
            self.fields['groups'].queryset = Group.objects.all()
        else:
             self.fields['groups'].queryset = Group.objects.filter(name__in=['CLIENTE', 'VENDEDOR'])
            #  self.fields['groups'].queryset = Group.objects.filter(name__in=['CLIENTE', 'VENDEDOR'])