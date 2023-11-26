from django.contrib import admin

from gestion_pedidos.models import clientes, articulos, pedidos

# Register your models here.

#asi agregamos una casilla de busqueda
class clientes_admin(admin.ModelAdmin):
    
    list_display=("nombre", "tlfno", "direccion")
    search_fields=("nombre", "tlfno")
   
#agregamos un filtro para datos en la tabla 
class articulos_admin(admin.ModelAdmin):
    list_filter=("seccion",)
    list_display=("nombre", "precio")
    search_fields=("nombre",)
    
class pedidos_admin(admin.ModelAdmin):
    list_display=("numero", "fecha")
    date_hierarchy="fecha"
    list_filter=("fecha",)


  
    
    
#agregamos las clases editadas donde corresponden
admin.site.register(clientes,clientes_admin)
admin.site.register(articulos, articulos_admin)
admin.site.register(pedidos, pedidos_admin)
