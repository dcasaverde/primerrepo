from django.urls import path
from . import views

urlpatterns = [
    path('listar', views.listar, name='listar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('crear', views.crear, name='crear'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]