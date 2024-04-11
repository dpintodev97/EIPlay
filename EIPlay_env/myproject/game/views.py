from django.shortcuts import render

# Create your views here.

#Necesitamos definir la vista de la app (game/views.py) que renderice (esto lo hace el navegador web) el archivo html
# estático.
#Este HTML es eltípico index.html, que en  un Django project está guardado en la carpeta de la app :
# game/tempaltes/index.html  :
def home(request):
    return render(request, 'index.html')

