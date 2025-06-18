from django.urls import path
from . import views
from django.conf.urls.i18n import set_language  # Import Django's language switcher

urlpatterns = [
    path('', views.home, name='home'),  
    path('set_language/', set_language, name='set_language'),  # Language switching
]
