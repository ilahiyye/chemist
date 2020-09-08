from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='api_index'),
    path('companies/', views.companies_listing, name='companies_listing'),
    path('companies/<uuid:uuid>/', views.company_items_listing, name='company_items_listing'),
    path('items/', views.items_listing, name='items_listing'),
    path('ingredients/', views.ingredients_listing, name='ingredients_listing'),
    path('packagings/', views.packaging_listing, name='packaging_listing'),
    path('ingredients/<uuid:uuid>/', views.ingridient_items_listing, name='views.ingredients_items_listing'),


]