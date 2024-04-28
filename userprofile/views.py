from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group, User
from django.contrib.auth import login
from django.contrib import messages

from django.utils.text import slugify

from django.db.models import Avg

from posts.models import Product

from .models import UserProfile

from posts.forms import ProductForm, UserForm, AccountForm, SignupForm
from reviews.models import ReviewDetails, Reseña

def es_vendedor(request):
    return request.groups.filter(name='Emprendedores').exists()

@login_required(login_url='log-in')
def cambiar_sub(request):
    if not es_vendedor(request.user):
        user = request.user
        return render (request, 'userprofile/change_sub.html', { 'user':user })
    else:
        return redirect('my-account')
    
@login_required(login_url='log-in')
def to_vendor(request):
    if not es_vendedor(request.user):
        user = request.user
        vendors = Group.objects.get(name='Emprendedores')
        vendors.user_set.add(user)

    return redirect('my-account')

def vendor_detail(request, pk):
    user = User.objects.get(pk=pk)
    products = user.products.filter(status=Product.ACTIVO)

    return render(request, 'userprofile/vendor_detail.html', {'user':user, 'products':products})

@login_required(login_url='log-in')
@user_passes_test(es_vendedor, login_url='change-subscription')
def my_posts(request):
    products = request.user.products.exclude(status=Product.ELIMINADO)

    return render(request, 'userprofile/my_posts.html', {'products':products})

@login_required(login_url='log-in')
@user_passes_test(es_vendedor)
def add_product(request):
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            title = request.POST.get('title')

            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()

            form.save_m2m()

            reviews = ReviewDetails.objects.create(product=product, promedio=0.0, comentarios=0)

            reviews.save()

            messages.success(request, 'Publicación creada')

            return redirect('my-posts')
    else:
        form = ProductForm()

    return render(request, 'userprofile/product_form.html', {'title':'Añadir publicación', 'form':form})

@login_required(login_url='log-in')
@user_passes_test(es_vendedor)
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)

    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()

            messages.success(request, 'Los cambios se han guardado correctamente')

            return redirect('my-posts')
    else:
        form = ProductForm(instance=product)

    return render(request, 'userprofile/product_form.html', {'title':'Editar publicación', 'form':form})

@login_required(login_url='log-in')
@user_passes_test(es_vendedor)
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.status = Product.ELIMINADO
    product.save()
    
    messages.success(request, 'La publicación se ha eliminado correctamente')

    return redirect('my-posts')

@login_required(login_url='log-in')
def myaccount(request):
    return render(request, 'userprofile/myaccount.html')

@login_required(login_url='log-in')
def editar_perfil(request, pk):
    user = UserProfile.objects.filter(user=request.user).get(pk=pk)

    if request.method=='POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Los cambios se han guardado correctamente')

            return redirect('my-account')
    else:
        form = UserForm(instance=user)

    return render(request, 'userprofile/profile_form.html', {'title':'Editar perfil', 'form':form})

@login_required(login_url='log-in')
def editar_cuenta(request):
    if request.method=='POST':
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Los cambios se han guardado correctamente')

            return redirect('my-account')
    else:
        form = AccountForm(instance=request.user)

    return render(request, 'userprofile/profile_form.html', {'title':'Editar cuenta', 'form':form})

@login_required(login_url='log-in')
def cambiar_contrasenya(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.POST)
    
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Los cambios se han guardado correctamente')

            return redirect('my-account')
        else:
            messages.warning(request, 'Ingrese los datos correctamente')
    else:
        form = PasswordChangeForm(request.POST)
    
    return render(request, 'userprofile/profile_form.html', { 'title':'Cambiar Contraseña', 'form':form })


def vendor_profile(request, pk):
    user = User.objects.get(pk=pk)

    return render(request, 'userprofile/vendor_profile.html', {'user':user})

def signup(request):
    if request.method=='POST':
        form = SignupForm(request.POST)
    
        if form.is_valid():
            user = form.save()

            login(request, user)

            userprofile = UserProfile.objects.create(user=user)

            return redirect('front-page')
    else:
        form = SignupForm()
    
    return render(request, 'userprofile/signup.html', { 'form':form })