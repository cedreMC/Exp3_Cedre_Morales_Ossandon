from django import forms
from .models import Jardineria
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class JardineriaForm(forms.ModelsForm):
    class Meta: 
        models = Jardineria
        fields = [ 'codigo', 'nombre', 'categoria', 'tipo', 'imagen']
        labels = {
            'codigo': 'codigo',
            'nombre' : 'nombre',
            'categoria' : 'categoria',
            'tipo' : 'tipo', 
            'imagen': 'Imagen'
        }
        widgets ={
            'codigo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese codigo..',
                    'id': 'codigo',
                    'class': 'form-control'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre..',
                    'id': 'nombre',
                    'class': 'form-control'
                }
            ),
            'categoria': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese categoria..',
                    'id': 'categoria',
                    'class': 'form-control'
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'id': 'tipo',
                    'class': 'form-control'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen',
                }
            )
            
        }
