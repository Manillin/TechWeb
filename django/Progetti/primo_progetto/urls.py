"""
URL configuration for primo_progetto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
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
from django.contrib import admin
from django.urls import path, re_path
from views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name="homepage"),
    path('parametri/', elenca_params, name='params'),
    path('paridispari', pari_dispari, name='paridispari'),
    re_path(r'^welcome_[A-Za-z0-9]+\/', greet_user, name='greetuser'),
    re_path(r'^$|^/$|home/$', homepage, name='homepage'),
    path('test/<str:nome>/<int:eta>', type_enforce_params, name='type_enforce'),
    path('hellotemplate/', hello_template, name='hellotemplate')
]


# es parametri -> assicurarsi che il parametro esista nel dizionario:
# if param not in request.GET (che è il dizionario): return Httpsblablabla("erorre")
