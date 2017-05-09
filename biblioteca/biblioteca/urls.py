"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url, include
from django.contrib import admin

from libros import views
from libros.views import ActualizarLibro, LibroLista, CrearLibro, LibroDetailView


urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^buscar/$', views.busqueda, name='busqueda'),
     url(r'^libros/$', views.lista_libros2, name='libros'),
     url(r'^detalle/(?P<object_id>\d+)/$', views.detalle_libro, name='detalle'),
     url(r'^detalle/(?P<slug>[\w-]+)/$', views.detalle_s, name='detalle_s'),
     url(r'^detalle/(?P<slug>[\w-]+)/$', views.detalle_slug, name='detalle_slug'),
     url(r'^detalle/(?P<object_id>\d+)/editar/$', views.actualizar, name='actualizar'),
     url(r'^crear_libro/$', views.agregar_libro, name='nuevo_libro'),
    # #Vistas basadas en clase
     url(r'^libros/lista/$', LibroLista.as_view(), name='List_view'),
     url(r'^libros/crear/$', CrearLibro.as_view(), name='create_view'),
     url(r'^libros/(?P<pk>\d+)/$', LibroDetailView.as_view(), name='detalle_view'),
     url(r'^libros/(?P<pk>\d+)/editar/$', ActualizarLibro.as_view(), name='update_view'),
     url(r'^libros/(?P<slug>[\w-]+)/$', LibroDetailView.as_view(), name='slug_detalle_view'),

    url(r'^admin/', admin.site.urls),
    url(r'^libros/', include("libros.urls", namespace='libros')),

]
