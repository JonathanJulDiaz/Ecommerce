"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from core.views import FrontPage, About, filter_products

urlpatterns = [
    path('about-us/', About.as_view(), name='about-us'),

    path('admin/', admin.site.urls),

    path('', include('userprofile.urls')),

    path('', include('posts.urls')),

    path('', FrontPage.as_view(), name='front-page'),

    #Filtrar
    path('filter-products/', filter_products, name="filter-product"),

    path("ckeditor5/", include('django_ckeditor_5.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)