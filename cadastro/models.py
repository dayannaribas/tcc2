from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, validate_ipv4_address
from django.db import models


class Cadastro(models.Model):
    conta_sid = models.CharField(max_length=34, verbose_name='Conta:', help_text='Nome da conta', validators=[
        RegexValidator(regex=r'^[a-zA-Z0-9]+$', message="Conta deve conter apenas letras ou números.",
                       code='erro_conta'), MinLengthValidator(limit_value=34), MaxLengthValidator(limit_value=34)])
    token_sid = models.CharField(max_length=34, verbose_name='Token:', help_text='Token de acesso', validators=[
        RegexValidator(regex=r'^[a-zA-Z0-9]+$', message="Token deve conter apenas letras ou números.",
                       code='erro_token'), MinLengthValidator(limit_value=32), MaxLengthValidator(limit_value=34)])
    servicos = models.CharField(max_length=34, verbose_name='Serviços', help_text='Nome do serviço', validators=[
        RegexValidator(regex=r'^[a-zA-Z0-9]+$', message="Serviço deve conter apenas letras ou números.",
                       code='erro_servico'), MinLengthValidator(limit_value=34), MaxLengthValidator(limit_value=34)])
    ligacao_de = models.CharField(
        max_length=14, verbose_name='Ligação de:', help_text='Número de origem. Ex: +5554988776655', validators=[
            RegexValidator(regex=r'^\+[0-9]+$', message="Formato de número inválido.", code='erro_numero_origem'),
            MinLengthValidator(limit_value=13), MaxLengthValidator(limit_value=14)])
    ligacao_para = models.CharField(
        max_length=14, verbose_name='Ligação para:', help_text='Número de destino. Ex: +5554988776655', validators=[
            RegexValidator(regex=r'^\+[0-9]+$', message="Formato de número inválido.", code='erro_numero_destino'),
            MinLengthValidator(limit_value=14), MaxLengthValidator(limit_value=14)])
    mensagem = models.CharField(max_length=20, verbose_name='Mensagem:', help_text='Mensagem a ser enviada')

    def __str__(self):
        return self.conta_sid
