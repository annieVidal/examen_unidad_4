from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import libromodelo
from .forms import libroAddForms, LibroModelForm

#4ta Unidad
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView


from biblioteca.multipleslugmixin import MultiSlug
#Parte de la BUSQUEDA
from django.db.models import Q
from django.shortcuts import render_to_response

# Create your views here.

################################################################


# Vistas basadas en clase

class CrearLibro(CreateView):
    model = libromodelo
    form_class = LibroModelForm
    success_url = "/libros/crear/"


    def get_context_data(self, *args, **kwargs):
        context = super(CrearLibro, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Crear"
        return context

class ActualizarLibro(UpdateView):
    model = libromodelo
    form_class = LibroModelForm
    success_url = "/libros/lista/"

    def get_context_data(self, *args, **kwargs):
        context = super(ActualizarLibro, self).get_context_data(*args, **kwargs)
        context["submit_btn"]="Editar"
        return context

class LibroDetailView(DetailView,MultiSlug):
    model = libromodelo
    # def get_object(self, *args, **kwargs):
    #     print self.kwargs
    #     slug = self.kwargs.get("slug")
    #     print slug
    #     ModelClass = self.model
    #     if slug is not None:
    #         try:
    #             libros = get_object_or_404(libromodelo, slug=slug)
    #             obj = get_object_or_404(ModelClass, slug=slug)
    #         except:
    #             libros = libromodelo.objects.filter(slug=slug).order_by("-nombre").first()
    #             obj = ModelClass.objects.filter(slug=slug).order_by("-nombre").first()
    #     else:
    #         obj = super(LibroDetailView, self).get_object(*args, **kwargs)

    #     return obj

class LibroLista(ListView):
    model = libromodelo

    def get_queryset(self, *args, **kwargs):
        qs = super(LibroLista, self).get_queryset(**kwargs)
        query=self.request.GET.get("q")
        qs=qs.filter(
                    Q(nombre__icontains=query)|
                    Q(autor__icontains=query)
                    ).order_by("nombre")
        print query
        return qs
        
        #return qs
#########

#BUSQUEDA

#def busqueda(request):
#    query = request.GET.get('q', '')
#    if query:
#        qset = (
#            Q(nombre__icontains=query) |
#            Q(autor__icontains=query)
#        )
#        results = libromodelo.objects.filter(qset).distinct()
#    else:
#        results = []
#    return render_to_response("busqueda.html", {
#        "results": results,
#        "query": query
#    })


################################################################

def home(request):
    mensaje="Bienvenido a la Bibioteca :D"
    send={"me":mensaje}
    return render(request, 'home.html',send)


def lista_libros2(request):
    #Logico de negocio alias hechizo
    librosclass = libromodelo.objects.all()
    print request
    m = "libro nuevo"
    template = "lista_libros.html"
    contexto= {"mensaje":m,
               "libros": librosclass }
    return render(request, template, contexto)

def detalle_libro(request, object_id=None):
    #Logico de negocio alias hechizo
    librosclass2 = get_object_or_404(libromodelo, id=object_id)
    m = "libro nuevo"
    template = "detalle.html"
    contexto= {"mensaje":m,
               "libros": librosclass2 }
    return render(request, template, contexto)

def detalle_s(request, slug=None):
    try:
        libroclass = get_object_or_404(libromodelo, slug=slug)
    except libromodelo.MultipleObjectsReturned:
        libroclass = libromodelo.objects.filter(slug=slug).order_by("-nombre").first()
    m = "libro nuevo"
    template = "detalle.html"
    contexto= {"mensaje":m,
           "producto": libroclass }
    return render(request, template, contexto)

def detalle_slug(request, slug=None):
    try:
        libroclass = get_object_or_404(libromodelo, slug=slug)
    except libromodelo.MultipleObjectsReturned:
        libroclass = libromodelo.objects.filter(slug=slug).order_by("-nombre").first()
    m = "libro nuevo"
    template = "detalle.html"
    contexto= {"mensaje":m,
           "producto": libroclass }
    return render(request, template, contexto)

def agregar_libro(request, object_id=None):
    form = LibroModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        print "Alta exitosa!"
    """
    if request.method == "POST":
        print request.POST
    if form.is_valid():
        # print request.POST
        data = form.cleaned_data
        nombre = data.get("nombre")
        autor = data.get("autor")
        editorial = data.get("editorial")
        ISBN = data.get("ISBN")
        precio = data.get("precio")
        # nuevo_producto = Producto.object.create(nombre = nombre,
        #                                         descripcion = descripcion,
        #                                         precio = precio)
        nuevo_libro = libromodelo()
        nuevo_libro.nombre = nombre
        nuevo_libro.autor = autor
        nuevo_libro.editorial = editorial
        nuevo_libro.ISBN = ISBN
        nuevo_libro.precio = precio
        nuevo_libro.save()
    """
    template = "agregar_libro.html"
    context = {
        "titulo":"Crear Producto!",
        "form":form
    }

    return render(request, template, context)


def actualizar(request, object_id=None):
    #Logico de negocio alias hechizo
    libros = get_object_or_404(libromodelo, id=object_id)
    form = LibroModelForm(request.POST or None, instance=libros)
    if form.is_valid():
        form.save()
        print "Actualizacion exitosa!"
    template = "actualizar.html"
    contexto= {
           "libros": libros,
           "form":form,
           "titulo":"Actualizar Libro"
           }
    return render(request, template, contexto)
