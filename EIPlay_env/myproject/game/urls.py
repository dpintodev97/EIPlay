from django.urls import path
from . import views

urlpatterns = [
    #path('registro/', views.registro, name='registro'),
    path('', views.registro, name='registro'),
    path('game/', views.home, name = 'home')
    # Otras URLs de la aplicación game...

#Con esta configuración, cuando un usuario visite la raíz del sitio, será redirigido a la página de registro/inicio de sesión.
# Y cuando accedan a /game/, se mostrará la página del juego.


]
#urlpatters: Define una lista llamada urlpatterns, que es una lista de todas las rutas URL disponibles
# en esta aplicación (la principal, la que lleva al contenido con preguntas.........)

#esta configuración establece que cuando un usuario accede a la ruta URL raíz de la aplicación
# (es decir, http://tudominio.com/), Django llamará a la función de vista home para manejar la solicitud.
# La URL también se identifica con el nombre 'home', que puede ser útil para generar enlaces dentro de
# la aplicación de forma dinámica.


