from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from posts.models import Product

from userprofile.models import UserProfile

def frontpage(request):
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

    return render(request, 'core/frontpage.html', content)

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