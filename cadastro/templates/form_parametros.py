from django import forms


class ParametrosForm(forms.ModelForm):
    class Meta:
        model = id
        fields = ["conta_sid", "token_sid", "servicos", "ligacao_de", "ligacao_para", "mensagem"]
