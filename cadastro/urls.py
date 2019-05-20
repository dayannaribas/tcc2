# -*- coding: utf-8 -*-
from django.urls import path
from .views import ligar, parametros, home, logout_view, mensagem_view

urlpatterns = [
    path('', home, name='home'),
    path('parametros', parametros, name='parametros'),
    path('ligacao', ligar, name='ligar'),
    path('mensagem', mensagem_view, name='mensagem'),
    path('logout', logout_view, name='logout'),
]
