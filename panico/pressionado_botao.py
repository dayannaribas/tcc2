import MQTT_recebe_tudo as topicos_recebidos
from panico.ligacao import TwilioService


#def botao_pressionado():
    if topicos_recebidos.TopicoSubscribe == "day/tele/buttonpanic":
        topicos_recebidos.on_message
        twilioservice.realiza_chamada("é a menssagem", "de=instance.cadastro.ligacao_de",
                             "para=instance.ligacao_para")