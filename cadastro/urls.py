# -*- coding: utf-8 -*-
from django.urls import path
from .views import parametros, home, logout_view, ligacao_view

urlpatterns = [
    path('', home, name='home'),
    path('parametros', parametros, name='parametros'),
    path('ligacao', ligacao_view, name='ligacao'),
    path('logout', logout_view, name='logout'),
]
