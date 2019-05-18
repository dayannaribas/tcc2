# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:01:07 2019

@author: d.ayanna
"""

import time
import paho.mqtt.client as paho
from decouple import config


broker_url = config('broker_url', default='0.0.0.0')


def publish_mqtt(broker, topic, message):

    # Define o objeto cliente mqtt
    client = paho.Client("client-001")

    # Conectando ao servidor
    print("connecting to broker ", broker)
    client.connect(broker)  # connect

    # Publica o tópico
    print("publishing ")
    client.publish(topic, message)

    # Desconecta
    print('disconnect')
    time.sleep(4)
    client.disconnect()

    # Encerra o loop
    print('encerra loop')
    client.loop_stop()


def subscribe_mqtt(broker, topic):

    # # define callback
    # def on_log(client, userdata, level, buf):
    #     print("log: ", buf)

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
    client.subscribe("day/power/led1")  # ("day/stat/buttonpanic")

    # Desconecta
    print('desconectado')
    time.sleep(4)
    client.disconnect()

    # Encerra o loop
    print('encerra loop')
    client.loop_stop()


if __name__ == '__main__':
    publish_mqtt(broker=broker_url, topic='day/tele/buttonpanic', message='0')
    # subscribe_mqtt(broker=broker_url, topic='day/stat/buttonpanic',)
