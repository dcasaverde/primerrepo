from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import libro
from .forms import LibroForm

# Create your views here.

def listar(request):
    libros = libro.objects.all()    
    context = {'libros':libros}
    return render(request,'libros/listar.html',context)
def crear(request):
    form = LibroForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('listar')  
    context = {'form': form}    
    return render(request,'libros/crear.html',context)
def editar(request,id):
    libros = libro.objects.get(id=id)
    form = LibroForm(request.POST or None, instance=libros)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('listar')
    return render(request,'libros/editar.html',{'form':form})
def eliminar(request,id):
    libros = libro.objects.get(id=id)       
    libros.delete() 
    return redirect('listar')  