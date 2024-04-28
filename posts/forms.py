from django import forms

from django.contrib.auth.models import User, Group

from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from .models import Product

from reviews.models import Reseña

from userprofile.models import UserProfile

from django_ckeditor_5.widgets import CKEditor5Widget

class ProductForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["descripcion"].required = False

    class Meta:
        model = Product
        fields = ('categoria', 'subcategoria', 'titulo', 'descripcion', 'precio', 'imagenes', 'domicilio', 'inventario', 'tags')
        widgets = {
            'categoria': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-500 my-3'
            }),
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-500 my-3'
            }),
            'descripcion': CKEditor5Widget(attrs={
                'class': 'django_ckeditor_5'
            }),
            'precio': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-gray-500 my-3'
            }),
            'imagenes': forms.FileInput(attrs={
                'class': 'w-full p-2 border border-gray-500 my-3'
            }),
            'domicilio': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-500 my-3'
            }),
            'inventario': forms.Select(attrs={
                'class': 'w-full p-2 border border-gray-500 my-3'
            }),
        }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su usuario',
            'id': 'hello'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
            'id': 'hi',
        }))

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["about_me"].required = False

    class Meta:
        model = UserProfile
        fields = ('numero', 'instagram', 'imagen', 'edad', 'about_me')
        
        widgets = {
            'imagen': forms.FileInput(attrs={
                'class': 'w-1/4 p-2 border border-gray-500 my-3'
            }),
            'numero': forms.TextInput(attrs={
                'class': 'w-1/4 p-2 border border-gray-500 my-3'
            }),
            'instagram': forms.TextInput(attrs={
                'class': 'w-1/4 p-2 border border-gray-500 my-3'
            }),
            'edad': forms.NumberInput(attrs={
                'class': 'w-1/4 p-2 border border-gray-500 my-3'
            }),
            'about_me': CKEditor5Widget(attrs={
                'class': 'django_ckeditor_5'
            }),
        }

class AccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-1/4 p-2 border border-gray-500 my-3'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-1/4 p-2 border border-gray-500 my-3'
            }),
            'email': forms.TextInput(attrs={
                'class': 'w-1/4 p-2 border border-gray-500 my-3'
            }),
        }

class SignupForm(UserCreationForm):
    
    grupo = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True,
                                   empty_label=None,
                                   initial=Group.objects.first(),
                                   widget=forms.Select(attrs={
                                     'class':'form-control w-96 rounded-full drop-shadow-md bg-gray-400 duration-300 hover:bg-gray-600 focus:bg-gray-600 focus:ring-0 text-black',
                                   }))

    username = UsernameField(
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su usuario',
                }))
    
    first_name = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre',
                }))

    last_name = forms.CharField(
            widget=forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su apellido',
                }))
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña',
        }))
    
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su contraseña de nuevo',
        }))

    email = forms.EmailField(
            widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese su correo',
            }))

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', 'grupo')

class ReseñaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # it is required to set it False,
        # otherwise it will throw error in console
        self.fields["descripcion"].required = False

    """
    descripcion = forms.CharField(widget=CKEditor5Widget(attrs={
        'placeholder': "Dejanos una reseña"
    }))
    """

    

    class Meta:
        model = Reseña
        fields = ['descripcion', 'estrellas']

        widget = {
        'descripcion': CKEditor5Widget(attrs={
                'class': 'django_ckeditor_5'
            }),
        }