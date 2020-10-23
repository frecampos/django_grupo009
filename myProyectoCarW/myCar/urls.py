from django.contrib import admin
from django.urls import path, include
from .views import index,galeria,registro,login,cerrar,insumos,lista_insumos,eliminar_insumo,misionyvision,buscar,modificar

urlpatterns = [   
    path('',index,name='INDEX'),
    path('galeria/',galeria,name='GALE'),
    path('registro/',registro,name='REG'),
    path('login/',login,name='LOGIN'),
    path('logout_sesion/',cerrar,name='LOGOUT'),
    path('insumos/',insumos,name='INSUMOS'),
    path('lista_insumos/',lista_insumos,name='LISTAI'),
    path('eliminar_in/<id>/',eliminar_insumo,name='ELIMINARINSUMO'),
    path('misionyvision/',misionyvision,name='MYV'),
    path('buscar/<id>/',buscar,name='BUSCAR'),
    path('modificar/',modificar,name='MODIFICAR'),
]