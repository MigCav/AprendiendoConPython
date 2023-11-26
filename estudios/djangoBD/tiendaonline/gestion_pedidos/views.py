from django.shortcuts import render
from django.http import HttpResponse
from gestion_pedidos.models import articulos
from django.core.mail import send_mail
from django.conf import settings
from gestion_pedidos.forms import formulario_contacto

# Create your views here.

def busqueda_productos(request):
    
    return render(request, "busqueda_productos.html")

def buscar(request):
    
    #controlamos que no haga una busqueda en blanco
    if request.GET["prd"]:
        
        #mensaje="articulo buscado: %r" %request.GET["prd"]

        producto= request.GET["prd"]
        
        if len(producto > 20):
            mensaje = "texto de busqueda demasiado largo"
        
        else:
            #el icontains funcio como "like" en SQL
            articulo=articulos.objects.filter(nombre__icontains=producto)
        
            return render(request, "resultados_busqueda.html", {"articulos":articulo, "query": producto})
    
        
    else:
        
        mensaje="No has introducido nada"
        
        return HttpResponse(mensaje)

# def contacto(request):
    
#     if request.method=="POST":
        
#         asunto=request.POST["asunto"]
        
#         mensaje= request.POST["mensaje"] + request.POST["email"]
        
#         email_from=settings.EMAIL_HOST_USER
        
#         recibe=["miguelecabrerav@gmail.com"]
        
#         send_mail(asunto, mensaje, email_from, recibe)
        
#         return render(request, "gracias.html")
        
    
#     return render(request, "contacto.html")

def contacto(request):
    
    if request.method=="POST":
        
        miformulario= formulario_contacto(request.POST)
    
        if miformulario.is_valid():
            
            infoform= miformulario.cleaned_data
        
            #introducimos el asunto, mensaje, correo ingresado
            #correo del que se enviara el mensaje y el correo que recibe        
            send_mail(infoform["asunto"], infoform["mensaje"], infoform.get("email", ""),["miguelecabrerav@gmail.com"],)
        
            return render(request, "gracias.html")
    
        else:
            miformulario=formulario_contacto()
            
    return render(request, "formulario_contacto.html",{"form":formulario_contacto})
        
    