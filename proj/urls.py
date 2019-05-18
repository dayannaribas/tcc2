"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
    
    
    passar no 1º parametro o que vai depois da barra (no site) e no 2º o nome do arquivo URLS
    da pagina a ser exibida
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('cadastro.urls'), name='cadastro'),
    path('admin/', admin.site.urls),
] 
