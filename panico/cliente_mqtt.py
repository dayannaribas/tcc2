# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:01:07 2019

@author: d.ayanna
"""

import os
import time
import paho.mqtt.client as paho
from decouple import AutoConfig


config = AutoConfig(search_path=os.path.abspath(os.path.curdir))
broker_url = config('broker_url', default='0.0.0.0', cast=str)


def publish_mqtt(topic, message, broker=broker_url):

    # Define o objeto cliente mqtt
    client = paho.Client("client-001")

    # Conectando ao servidor
    print("Conectando ao servidor ", broker)
    client.connect(broker)  # connect

    # Publica o tópico
    print("Publica o tópico ")
    client.publish(topic, message)

    # Desconecta
    print('Desconecta')
    time.sleep(4)
    client.disconnect()

    # Encerra o loop
    print('Encerra o loop')
    client.loop_stop()


def subscribe_mqtt(topic, broker=broker_url):
      
    def on_message(client, userdata, message):
        while True:
            print('dormindo')
            time.sleep(1)
            print("received message =", str(message.payload.decode("utf-8")))

    # Define o objeto cliente mqtt
    client = paho.Client("client-001")

    # Define a função do callback
    client.on_message = on_message
    # client.on_log = on_log

    # Conectando ao servidor
    print("Conectando ao servidor broker ", broker)
    client.connect(broker)

    # Inicia um loop para receber a resposta do servidor
    client.loop_start()

    # Definindo o tópico a enviar
    print("definindo o topico para subescrever ")
    client.subscribe(topic) #"day/power/led1")  # ("day/stat/buttonpanic")

    # Desconecta
    print('desconectado')
    time.sleep(4)
    client.disconnect()

    # Encerra o loop
    print('encerra loop')
    client.loop_stop()


#if __name__ == '__main__':
#    #publish_mqtt(broker=broker_url, topic='day/tele/buttonpanic', message='0')
#    print(broker_url)
#    subscribe_mqtt(broker=broker_url, topic='day/stat/mq2')
