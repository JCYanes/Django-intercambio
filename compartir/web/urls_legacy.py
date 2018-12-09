from django.urls import path
from django.views.generic import RedirectView


urlpatterns = [
    path('index.php',RedirectView.as_view(url='/')),
    path('especial/condiciones-de-trueque.php',RedirectView.as_view(url='/condiciones-de-trueque/')),
    path('noticias/noticias.php',RedirectView.as_view(url='/noticias/')),
]
