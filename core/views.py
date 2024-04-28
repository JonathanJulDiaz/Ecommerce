from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from posts.models import Product

from userprofile.models import UserProfile

from django.template.loader import render_to_string

class FrontPage(View):
    template_name = 'core/frontpage.html'
    form_class = View
    products = Product.objects.filter(status=Product.ACTIVO)
    universities = UserProfile._meta.get_field('universidad').choices
    domicilio = Product._meta.get_field('domicilio').choices
    inventario = Product._meta.get_field('inventario').choices

    content = {
        'products': products,
        'universities': universities,
        'domicilio': domicilio,
        'inventario': inventario,
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.content)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-view'))
        else:
            return render(request, self.template_name, self.content)

class About(View):
    template_name = 'core/about.html'
    form_class = View
    content = {
        
    }
    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, self.content)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list-view'))
        else:
            return render(request, self.template_name, self.content)
        
def filter_products(request):
    university = request.GET.getlist('universidad[]')
    domicilios = request.GET.getlist('domicilio[]')
    inventarios = request.GET.getlist('inventario[]')

    products = Product.objects.filter(status=Product.ACTIVO).distinct()

    if len(domicilios) > 0:
        products = products.filter(domicilio__in=domicilios).distinct()
    if len(inventarios) > 0:
        products = products.filter(inventario__in=inventarios).distinct()
    if len(university) > 0:
        perfiles_usuario = UserProfile.objects.filter(universidad__in=university)

        # Obtener los IDs de los usuarios que tienen la universidad deseada
        ids_usuarios = perfiles_usuario.values_list('user_id', flat=True)

        # Filtrar los productos asociados a esos usuarios
        products = products.filter(user_id__in=ids_usuarios).distinct()

    data = render_to_string("posts/partials/products.html", { 'products': products })
    return JsonResponse({ "data": data })