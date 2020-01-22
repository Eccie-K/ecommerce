from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from cart.views import add_to_cart, remove_from_cart
from .views import Shop


app_name = 'mainapp'

urlpatterns =[
    url('^home$', views.home, name = 'home'),
    url('^products$', Shop.as_view(), name = 'products'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)