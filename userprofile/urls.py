from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

from posts.forms import UserLoginForm

urlpatterns = [
    #Ingreso
    path('sign-up/', views.signup, name='sign-up'),
    path('log-in/', auth_views.LoginView.as_view(template_name='userprofile/login.html', authentication_form=UserLoginForm), name='log-in'),
    path('log-out/', auth_views.LogoutView.as_view(), name='log-out'),

    #Mi cuenta
    path('my-account/', views.myaccount, name='my-account'),
    path('my-account/edit-profile/<int:pk>/', views.editar_perfil, name='edit-profile'),
    path('my-account/edit-account/', views.editar_cuenta, name='edit-account'),
    path('my-account/change-password/', views.cambiar_contrasenya, name='change-password'),
    path('my-account/change-subscription/', views.cambiar_sub, name='change-subscription'),
    path('a-vender/', views.to_vendor, name='a-vender'),

    #Mis publicaciones
    path('my-posts/', views.my_posts, name='my-posts'),
    path('my-posts/add-product/', views.add_product, name='add_product'),
    path('my-posts/edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('my-posts/delete-product/<int:pk>/', views.delete_product, name='delete_product'),

    #Publicaciones de vendedores
    path('vendors/<int:pk>/', views.vendor_detail, name='vendor-detail'),
    path('vendor-profile/<int:pk>/', views.vendor_profile, name='profile'),
]