# This code is defining the URL patterns for a Django application.
from django.urls import path
from. import views

urlpatterns = [
    
path('',views.login_view,name='login'),
 path('inicio', views.inicio, name='inicio'),   
 path('clientes',views.clientes, name='clientes'),
 path('clientes/crear',views.crear, name='crear'),
 path('clientes/editar',views.editar, name='editar'),
 path('eliminar/<int:id>',views.eliminar, name='eliminar'),
 path('clientes/editar/<int:id>',views.editar, name='editar'),
 path('exportarexcel', views.exportarexcel, name='exportarexcel'), 
 path('exportarexcel2', views.export_data_to_excel, name='exportar_excel'),



]