from django.db.models import Q
from django.db.models.manager import BaseManager
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Product, Category, Subcategory

from reviews.models import Reseña, ReviewDetails

from .forms import ReseñaForm

from userprofile.saved import Saved

from taggit.models import Tag

def search(request):
    query = request.GET.get('query','')
    products = Product.objects.filter(Q(titulo__icontains=query)|
                                      Q(descripcion__icontains=query), status=Product.ACTIVO)

    return render(request, 'posts/search.html', {'query':query, 'products':products})

def filter(request, products: BaseManager[Product]):
    query = request.GET.get('query','')
    products = products.filter(Q(titulo__icontains=query)|
                                      Q(descripcion__icontains=query), status=Product.ACTIVO)

    return render(request, 'posts/search.html', {'query':query, 'products':products})

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    products = Product.objects.filter(tags=tag)

    context = {
        'tag':tag,
        'products':products,
    }

    return render(request, 'posts/tags.html', context)

def subcategory_detail(request, slug, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(Subcategory, slug=slug)
    products = subcategory.products.filter(status=Product.ACTIVO)

    content = {
        'category': category,
        'subcategory':subcategory,
        'products': products
    }
    return render(request, 'posts/subcategory_detail.html', content)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.filter(status=Product.ACTIVO)

    content = {
        'category': category,
        'products': products
    }
    return render(request, 'posts/category_detail.html', content)

def product_detail(request, slug, category_slug, subcategory_slug):
    #Producto a mostrar
    product = get_object_or_404(Product, slug=slug, status=Product.ACTIVO)

    #Publicaciones relacionadas
    #Por el mismo usuario
    user_p = Product.objects.filter(user=product.user).exclude(pk = product.id)
    #Misma Categoria
    category_p = Product.objects.filter(categoria=product.categoria).exclude(pk = product.id)
    #Misma subcategoria
    subcategory_p = Product.objects.filter(subcategoria=product.subcategoria).exclude(pk = product.id)

    #All reviews of the products
    reviews = Reseña.objects.filter(product=product).order_by("-created_at")

    #Average rating
    average = get_object_or_404(ReviewDetails, product=product).promedio

    #Cada estrella
    typeEstrellas = []
    typeEstrellas.append(Reseña.objects.filter(product=product, estrellas=1).count())
    typeEstrellas.append(Reseña.objects.filter(product=product, estrellas=2).count())
    typeEstrellas.append(Reseña.objects.filter(product=product, estrellas=3).count())
    typeEstrellas.append(Reseña.objects.filter(product=product, estrellas=4).count())
    typeEstrellas.append(Reseña.objects.filter(product=product, estrellas=5).count())

    #Estrella porcentaje
    porcentaje = []
    if average > 0.0 :
        porcentaje.append(int((typeEstrellas[0]*100)/len(reviews)))
        porcentaje.append(int((typeEstrellas[1]*100)/len(reviews)))
        porcentaje.append(int((typeEstrellas[2]*100)/len(reviews)))
        porcentaje.append(int((typeEstrellas[3]*100)/len(reviews)))
        porcentaje.append(int((typeEstrellas[4]*100)/len(reviews)))
    else:
        porcentaje.append(0)
        porcentaje.append(0)
        porcentaje.append(0)
        porcentaje.append(0)
        porcentaje.append(0)

    #Mostrar estrellas
    if int(average) < 5:
        showE = range(5 - int(average))
    else:
        showE = range(0)
    showE2 = range(int(average))

    #Review form
    review_form = ReseñaForm()

    return render(request, 'posts/product_detail.html', { 'product': product,
                                                         'reviews': reviews,
                                                         'average':average,
                                                         'typeEstrellas':typeEstrellas,
                                                         'porcentaje':porcentaje,
                                                         'review_form':review_form,
                                                         'showE':showE,
                                                         'showE2':showE2,
                                                         'user_p':user_p,
                                                         'category_p':category_p,
                                                         'subcategory_p':subcategory_p
                                                         })

@login_required(login_url='log-in')
def add_review(request, product_id):
    if request.method=='POST':
        form = ReseñaForm(request.POST)

        if form.is_valid():
            review = form.save(commit=False)

            review.user = request.user
            review.product = get_object_or_404(Product, pk = product_id)
            review.descripcion = request.POST.get('descripcion')
            review.estrellas = request.POST.get('estrellas')
            review.save()

            form.save_m2m()

            form = ReseñaForm()

            return redirect('front-page')
    else:
        form = ReseñaForm()

    return render(request, 'posts/partials/review_form.html', {'review_form':form})

@login_required(login_url='log-in')
def add_to_saved(request, product_id):
    saved = Saved(request)
    saved.add(product_id)

    return redirect('saved_view')

@login_required(login_url='log-in')
def remove_from_saved(request, product_id):
    saved = Saved(request)
    saved.remove(product_id)

    return redirect('saved_view')

@login_required(login_url='log-in')
def saved_view(request):
    saved = Saved(request)

    return render(request, 'posts/saved_view.html', { 'saved': saved })