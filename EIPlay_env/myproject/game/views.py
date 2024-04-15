from django.shortcuts import render, redirect

# Create your views here.

#Necesitamos definir la vista de la app (game/views.py) que renderice (esto lo hace el navegador web) el archivo html
# estático.
#Este HTML es el típico index.html, que en  un Django project está guardado en la carpeta de la app :
# game/tempaltes/index.html  :
def home(request):
    #return HttpResponse('holi')
   return render(request, 'index.html')

