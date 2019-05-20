from auditlog.registry import auditlog
from django.core.validators import RegexValidator, MaxLengthValidator, MinLengthValidator, validate_ipv4_address
from django.db import models


def get_actual_content(obj, key):
    actual_content = ''
    if obj.objects.last():
        actual_content = obj.objects.last().__dict__
        actual_content = actual_content[key]
    return actual_content


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
    broker = models.CharField(
        max_length=13, verbose_name='Broker:', help_text='IP do servidor MQTT. Ex: 192.168.100.107',
        validators=[validate_ipv4_address], default='')

    def __str__(self):
        return self.conta_sid


auditlog.register(Cadastro)
