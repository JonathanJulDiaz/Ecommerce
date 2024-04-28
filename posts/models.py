from django.db import models

from autoslug import AutoSlugField

from django.contrib.auth.models import User

from taggit.managers import TaggableManager

from django_ckeditor_5.fields import CKEditor5Field

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title',editable=True, always_update=True)

    class Meta:
        verbose_name = ('Categoria')
        verbose_name_plural = ('Categorias')

    def __str__(self):
        return self.title
    
class Subcategory(models.Model):
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE, verbose_name='category', default=2)
    title = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='title',editable=True, always_update=True)

    class Meta:
        verbose_name = ('Subcategoria')
        verbose_name_plural = ('Subcategorias')

    def __str__(self):
        return self.title

class Product(models.Model):
    PROCESADO = 'procesado'
    ESPERANDO_APROBACION = 'esperando_aprobacion'
    ACTIVO = 'activo'
    ELIMINADO = 'eliminado'

    OPCIONES_DE_ESTADO = [
        (PROCESADO, 'Procesado'),
        (ESPERANDO_APROBACION, 'Esperando aprobación'),
        (ACTIVO, 'Activo'),
        (ELIMINADO, 'Eliminado')
    ]

    user = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE, verbose_name='user')
    categoria = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE, default=15)
    titulo = models.CharField(max_length=45)
    slug = AutoSlugField(populate_from='titulo',editable=True, always_update=True)
    descripcion = CKEditor5Field(blank=True)
    precio = models.PositiveIntegerField(default=0)
    domicilio = models.CharField(choices={
        'NO':'Solo dentro de la universidad',
        'SI':'Se hacen domicilios fuera de la universidad'
    }, default='NO', max_length=2)
    inventario = models.CharField(choices={
        'LIMITADO':'Venta limitada',
        'INFINITO':'Venta sin limite'
    }, default='LIMITADO', max_length=8)
    imagenes = models.ImageField(upload_to='uploads/product_images/', blank=True, null=True)
    tags = TaggableManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=OPCIONES_DE_ESTADO, default=ACTIVO)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.titulo

    def get_display_price(self):
        precio = "{:,}".format(self.precio)
        return precio
    
    def get_display_image(self):
        return self.imagenes
    
    def get_status(self):
        return self.status.__getitem__(1)