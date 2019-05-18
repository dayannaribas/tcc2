from django import forms
from .models import *


class ParametrosForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ["conta_sid", "token_sid", "servicos", "ligacao_de", "ligacao_para", "mensagem"]
