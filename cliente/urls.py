# This code is defining the URL patterns for a Django application.
from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static

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

 path('ventas',views.ventas, name='ventas'),
 path('ventas/crear',views.crear_ventas, name='crear_ventas'),
 path('ventas/editar',views.editar_ventas, name='editar_ventas'),
 path('ventas/eliminar/<int:id>',views.eliminar_ventas, name='eliminar_ventas'),
 path('editarVentas/<int:id>',views.editar_ventas, name='editar_ventas'),
 
 path('graficas', views.graficas,name='graficas'),
 path('graficas2', views.grafico,name='grafico'),

]+static(settings.MEDIA_URL,documents_root=settings.MEDIA_ROOT)