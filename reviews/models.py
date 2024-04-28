from django.db import models

from django.db.models import Avg

from django.contrib.auth.models import User

from django_ckeditor_5.fields import CKEditor5Field

from posts.models import Product

class Reseña(models.Model):
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='resena', on_delete=models.CASCADE)

    descripcion = CKEditor5Field(max_length=150, null=False, blank=False)
    estrellas = models.PositiveIntegerField(choices=((1, '1 estrella'),(2, '2 estrellas'),(3, '3 estrellas'),(4, '4 estrellas'),(5, '5 estrellas')),
                                            default=5)

    like = models.PositiveIntegerField(null=False, blank=False, default=0)
    dislike = models.PositiveIntegerField(null=False, blank=False, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('product', 'user')
        ordering = ['-created_at']
        verbose_name = ('Reseña')
        verbose_name_plural = ('Reseñas')

    def save(self, *args, **kwargs):
        super(Reseña, self).save(*args, **kwargs)
        review = ReviewDetails.objects.get(product=self.product)
        review.promedio = Reseña.objects.filter(product=self.product).aggregate(rating=Avg('estrellas'))['rating']
        review.comentarios = Reseña.objects.filter(product=self.product).count()
        review.save()

    def delete(self, *args, **kwargs):
        super(Reseña, self).delete(*args, **kwargs)
        review = ReviewDetails.objects.get(product=self.product)
        review.promedio = Reseña.objects.filter(product=self.product).aggregate(rating=Avg('estrellas'))['rating']
        review.comentarios = Reseña.objects.filter(product=self.product).count()
        review.save()

    def __str__(self):
        return self.product.titulo
    
    def get_estrellas(self):
        list = []
        for i in range(self.estrellas):
            list.append(i)
        return list
    

class ReviewDetails(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)

    promedio = models.FloatField(null=False, blank=False, default=0.0)
    
    comentarios = models.IntegerField(null=False,blank=False, default=0)

    class Meta:
        verbose_name = ('Detalle de Reseña')
        verbose_name_plural = ('Detalles de Reseñas')