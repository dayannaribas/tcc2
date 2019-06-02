import paho.mqtt.client as mqtt
import os
import json
import sys
sys.path.append('../')
from gas.naive_bayes import *

# from package import item
# import package


# definicoes: 
Broker = "139.59.215.85"
PortaBroker = 1883
KeepAliveBroker = 60
TopicoSubscribe = "day/tele/#"


# Callback - conexao ao broker realizada
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conectado ao Broker. Resultado de conexao: "+str(rc))

    # faz subscribe automatico no topico
    client.subscribe(TopicoSubscribe)


# Callback - mensagem recebida do broker
def on_message(client, userdata, msg):

    retorno = json.loads(msg.payload)
#    print(retorno)

#    if "gas" in retorno:
#        modelo = Modelo()
#        status = modelo.modelo_navie_base(retorno["gas"],
#                                          retorno["temperatura"],
#                                          retorno["umidade"])
#        print("Tem vazamento? ", status)

    if "valvula" in retorno:
        print("gas ", retorno["valvula"])


#    if "buttonpanic" in retorno:
#        if retorno["buttonpanic"] == 1:
#            print('Executando ligacao')
#            from panico.ligacao import TwilioService
#            twilio_service = TwilioService()
#            twilio_service.realiza_chamada("essa eh menssagem do botao")
#            time.sleep(5)
#
#    if "ipbotao" in retorno:
#        print("IP do botao ")

#    if "ipmodulo" in retorno:
#        print("IP do modulo ")
#
#
#    if "fumaca" in retorno:
#        print("FUMACA ",retorno["fumaca"])

    if "temperature" in retorno:
        print("Temperatura ", retorno["temperature"])

    if "humidity" in retorno:
        print("Umidade", retorno["humidity"])

#    if "ledLigado" in retorno:
#        print("minha função status da Lampada")

#    if "lamp" in retorno:
#        print("minha função Lampada")


# programa principal:
try:
        print("[STATUS] Inicializando MQTT...")
        # inicializa MQTT:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(Broker, PortaBroker, KeepAliveBroker)
        client.loop_forever()


except KeyboardInterrupt:
        print("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
        sys.exit(0)
