"""
URL configuration for project project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path
# HTTP Request <-> HTTP Response
# MVT (MVC)


# Essa é uma função de visualização simples que imprime uma mensagem no console
def my_view(request):
    print('posso fazer outras coisas')
    return HttpResponse('Uma mensagem para alguém especial')


# Função de visualização para a página inicial
def home(request):
    print('home')
    return HttpResponse('home1')


# Função de visualização para a página de blog
def blog(request):
    print('blog')
    return HttpResponse('blog')


# Lista de URLs do aplicativo
urlpatterns = [
    path('', home),  # URL raiz para a página inicial
    path('blog/', blog),  # URL para a página do blog
    path('admin/', admin.site.urls),  # URL para o painel de administração
    path('blog/', my_view),  # URL para a função de visualização 'my_view'
]
