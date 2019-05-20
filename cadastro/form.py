from django import forms
from .models import Cadastro, Mensagem, get_actual_content


class ParametrosForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ParametrosForm, self).__init__(*args, **kwargs)
        self.instance = getattr(self, 'instance', None)

        cadastro = Cadastro
        for key, value in self.fields.items():
            value.initial = get_actual_content(cadastro, key)

    class Meta:
        model = Cadastro
        fields = ["broker", "conta_sid", "token_sid", "servicos", "ligacao_de"]


class MensagemForm(forms.ModelForm):

    class Meta:
        model = Mensagem
        fields = ["ligacao_para", "mensagem"]
