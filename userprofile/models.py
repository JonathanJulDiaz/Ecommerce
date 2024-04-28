from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django_ckeditor_5.fields import CKEditor5Field

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="userprofile", on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    edad = models.PositiveSmallIntegerField(null=False, blank=False, default=18)
    about_me = CKEditor5Field(null=True, blank=True, max_length=150)
    instagram = models.CharField(null=True, max_length=15, blank=True)
    universidad = models.CharField(choices={
        'EAFIT':'Universidad EAFIT',
        'UDEA':'Universidad de Antioquia',
        'CES':'Universidad CES',
        'UPB':'Universidad Pontificia Bolivariana',
        'ANDES':'Universidad de los Andes',
    }, default='EAFIT', max_length=5)
    imagen = models.ImageField(upload_to='uploads/userprofile/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.user.username
    
    def get_display_number(self):
        return "https://web.whatsapp.com/send/?phone=57"+self.numero+"/"
    
    def get_display_instagram(self):
        return "https://www.instagram.com/"+self.instagram+"/"
    
    def get_display_university(self):
        return self.universidad
    
    def am_vendor(self):
        return self.user.groups.filter(name='Emprendedores').exists()
    
    def get_posts(self):
        return self.product_set.objects.all()
    
    def get_comments(self):
        return self.comentario_set.objects.all()
    
def create_profile(sender, instance, created, **kwargs):
     if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)