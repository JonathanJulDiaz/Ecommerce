from django.urls import path

from . import views

urlpatterns = [
    #Buscar
    path('search/', views.search, name='search'),

    #Guardados
    path('add-to-saved/<int:product_id>/', views.add_to_saved, name='add-to-saved'),
    path('remove-from-saved/<str:product_id>/', views.remove_from_saved, name='remove-from-saved'),
    path('saved/', views.saved_view, name='saved-view'),

    #Filtrar
    path('filter-products/', views.filter_products, name="filter-product"),

    #Ordenar
    path('order-products/', views.order_products, name="order-product"),

    #Diferentes filtros
    path('<slug:slug>/', views.category_detail, name='category-detail'),
    path('<slug:category_slug>/<slug:slug>', views.subcategory_detail, name='subcategory-detail'),
    path('tag/<slug:slug>/', views.tagged, name='tagged'),

    #Detalles de la publicación
    path('<slug:category_slug>/<slug:subcategory_slug>/<slug:slug>/', views.product_detail, name='product-detail'),

    #Reseña
    path('add-review/<int:product_id>/', views.add_review, name='add-review'),
]