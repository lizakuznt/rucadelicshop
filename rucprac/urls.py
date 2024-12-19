from django.contrib import admin
from django.urls import path, include

from rucprac import views

urlpatterns = [
    path('index/', views.index, name=''),
    path('catalog/', views.catalog, name='catalog'),
    #path('catalog/catalog_2/', views.catalog_2, name='catalog_2'),
    path('catalog/catalog_2/add_product/', views.add_product, name='add_product'),
    path('catalog/about_product/<int:product_id>/', views.product_about, name='about_product'),
    path('catalog/update_product/<int:product_id>/', views.product_update, name='product_update'),
    path('catalog/feedback/', views.feedback, name='feedback'),
    path('catalog/tag/list/', views.list_tag, name='list_tag'),
    path('catalog/tag/<int:tag_id>/', views.tag_products, name='tag_products'),
    path('catalog/category/list/', views.array_category, name='array_category'),
    path('catalog/category/<int:category_id>', views.category_products, name='category_products'),
    path('catalog/category/add/', views.add_category, name='add_category'),
]