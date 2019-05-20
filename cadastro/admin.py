from django.contrib import admin

# Register your models here.
from .models import Cadastro, Mensagem

admin.site.register(Cadastro)
admin.site.register(Mensagem)
