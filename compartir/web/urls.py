from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index),
    path('condiciones-de-trueque/', views.conditions),
    path('categorias/<str:title>_<int:code>', views.category),
    path('nuevos productos/', views.productsnew),
    path('noticias/', views.news),
    path('noticias/<str:title>_<int:code>', views.new),
    path('producto/<str:title>_<int:code>',views.product),
    path('',include('web.urls_legacy')),
]
