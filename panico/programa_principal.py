import os
from decouple import AutoConfig
from .ligacao import realiza_chamada
from .cliente_mqtt import publish_mqtt, subscribe_mqtt

config = AutoConfig(search_path=os.path.abspath(os.path.curdir))

broker_url = config('broker_url', default='0.0.0.0')
telefone_origem = config('telefone_origem', default='')
telefone_destino = config('telefone_destino', default='')

if __name__ == '__main__':
    realiza_chamada(mensagem="Ola! estou em perigo!", de=telefone_origem, para=telefone_destino)

