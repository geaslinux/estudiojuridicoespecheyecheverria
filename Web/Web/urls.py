"""Web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from Core import views as Core_views
from Noticias import views as Noticias_views


from django.conf import settings

urlpatterns = [
    path('', Core_views.inicio, name="Inicio"),
    path('Quienes Somos/', Core_views.quienessomos, name="Quienes Somos"),
    path('Noticias/', Noticias_views.noticias, name="Noticias"),
    path('Servicios/', Core_views.servicios, name="Servicios"),
    path('Cursos/', Core_views.cursos, name="Cursos"),
    path('Contacto/',Core_views.contacto, name="Contacto"),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)