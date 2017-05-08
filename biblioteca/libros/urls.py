#4taUnidad

from django.conf.urls import url
from django.contrib import admin

from libros import views
from libros.views import ActualizarLibro, LibroLista, CrearLibro, LibroDetailView

urlpatterns = [

    url(r'^lista/$', LibroLista.as_view(), name='List_view'),
    url(r'^crear/$', CrearLibro.as_view(), name='create_view'),
    url(r'^(?P<pk>\d+)/$', LibroDetailView.as_view(), name='detalle_view'),
    url(r'^(?P<pk>\d+)/editar/$', ActualizarLibro.as_view(), name='update_view'),
    url(r'^(?P<slug>[\w-]+)/$', LibroDetailView.as_view(), name='slug_detalle_view'),

]
