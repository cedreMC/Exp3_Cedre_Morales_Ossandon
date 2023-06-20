from django.urls import path
from .views import Principal1, otra,crear,eliminar,modificar, registrar, mostrar, segundo , tercero, Decertico, Formulario

urlpatterns=[
    path('', Principal1, Name="Principal1"),
    path('otra/', otra, name="otra"),
    path('crear/', crear, name="crear"),
    path('eliminar/<id>', eliminar, name="eliminar"),
    path('modificar/<id>', modificar, name="modificar"),
    path('registrar/', registrar, name="registrar"),
    path('mostrar/',mostrar, name="mostrar"),
    path('segundo/', segundo, name="segundo"),
    path('tercero/', tercero, name="tercero"),
    path('Decertico/<id>', Decertico, name="Decertico"),
    path('Formulario/<id>', Formulario, name="Formulario")
    
]