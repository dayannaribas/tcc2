from django.contrib import admin

# Register your models here.
from .models import Cadastro, Ligacao

admin.site.register(Cadastro)
admin.site.register(Ligacao)
