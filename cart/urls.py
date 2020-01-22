from django.conf.urls import url 
from django.conf import settings 
from . import views
from django.conf.urls.static import static

urlpatterns = [

    url('cart/<slug>', views.add_to_cart , name = 'add_to_cart'),
    url('remove/<slug>', views.remove_from_cart, name = 'remove_from_cart')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)