from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home')
]
#urlpatters: Define una lista llamada urlpatterns, que es una lista de todas las rutas URL disponibles
# en esta aplicación (la principal, la...)

#esta configuración establece que cuando un usuario accede a la ruta URL raíz de la aplicación
# (es decir, http://tudominio.com/), Django llamará a la función de vista home para manejar la solicitud.
# La URL también se identifica con el nombre 'home', que puede ser útil para generar enlaces dentro de
# la aplicación de forma dinámica.


