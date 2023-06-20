from django.shortcuts import render, redirect
from .models import Jardineria
from .forms import JardineriaForm, RegistroUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

# Create your views here.

def Principal1(request):
     return render(request, 'Principal1.html')

@login_required
def otra(request):
     jardinerias = Jardineria.objects.raw('select * from Jardinerias_jardineria')
     datos={
          'autitos':jardinerias
     }
     return render(request, 'otra.html', datos)

@login_required
def crear(request):
     if request.method=="POST":    
          jardineriaForm = JardineriaForm(request.POST, request.FILES)    #creamos un objeto de tipo Formulario
          if jardineriaForm.is_valid():
               jardineriaForm.save()      #similar al insert de sql en función 
               return redirect('otra')
     else: 
          JardineriaForm=JardineriaForm()
     return render(request, 'crear.html', {'Jardineria_form':JardineriaForm})



@login_required
def eliminar(request, id):
     JardineriaEliminado = Jardineria.objects.get(patente=id)   
     JardineriaEliminado.delete()
     return redirect ('otra')

@login_required
def modificar(request, id):
     JardineriaModificado=Jardineria.objects.get(patente=id)
     datos = {
          'form' : JardineriaForm(instance=JardineriaModificado)
     }
     if request.method=='POST':
          formulario = JardineriaForm(data=request.POST, instance=JardineriaModificado)
          if formulario.is_valid:
               formulario.save()
               return redirect('otra')
     return render(request, 'modificar.html', datos)


def registrar(request):
     data={
          'form' : RegistroUserForm()
     }
     if request.method=="POST":
          formulario = RegistroUserForm(data=request.POST)
          if formulario.is_valid():
               formulario.save()
               user=authenticate(username=formulario.cleaned_data["username"],
                                 password=formulario.cleaned_data["password1"])
               login(request, user)
               return redirect('index')
          data["form"]=formulario
     return render(request, 'registration/registrar.html',data)

@login_required
def mostrar(request):
     autitos = Jardineria.objects.all()
     datos={
          'autitos':autitos
     }
     return render(request, 'mostrar.html', datos)

