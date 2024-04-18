from django.shortcuts import render, redirect

# Create your views here.

#Necesitamos definir la vista de la app (game/views.py) que renderice (esto lo hace el navegador web) el archivo html
# estático.
#Este HTML es el típico index.html, que en  un Django project está guardado en la carpeta de la app :
# game/tempaltes/index.html  :
def home(request):
    #return HttpResponse('holi')
   return render(request, 'index.html')
#FUNCION QUE ANTE LA SOLICITUD, RETORNA EL index.html, QUE ES LA PAGINA PRINCIPAL DE LA APP

#NOTA: NECESITAMOS OTRAS RESPUESTAS A OTRAS SOLICTUDES, SEGUN EL USUARIO NAVEGUE POR LA WEB

def contenido(request):
    return render(request, 'contenido.html')
#RETORNO, REMITA AL USER A LA PAGINA DE PREGUNTAS, DONDE PODRÁ RESOLVERLAS

def contenido(request):
    return render(request, 'contenido.html')
#URL QUE LLEVE AL HTML DINÁMICO, DONDE CON UN SOLO HTML, VAYA CARGÁNDOSE LAS PREGUNTAS ALMACENADAS EN LA BBDD

def registro(request):
    return render(request)


