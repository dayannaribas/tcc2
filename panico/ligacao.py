# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from decouple import AutoConfig

config = AutoConfig(search_path=os.path.abspath(os.path.curdir))


class TwilioService(object):
    def __init__(self):
        self.account_sid = config('account_sid', default='', cast=str)
        self.auth_token = config('auth_token', default='', cast=str)
        self.client = Client(self.account_sid, self.auth_token)
        self.telefone_origem = config('telefone_origem', default='')
        self.telefone_destino = config('telefone_destino', default='')

    def realiza_chamada(self, mensagem):

        # https://www.twilio.com/labs/twimlets/echo -
        default_url = "http://twimlets.com/echo?Twiml=%3CResponse%3E%0A%3CSay%20language%3D'pt-BR'%20voice%3D%22alice%2\
2%3E{}%3C%2FSay%3E%0A%3C%2FResponse%3E&"
        message_ = mensagem.replace(" ", "%20")
        url = default_url.format(message_)
        call = self.client.calls.create(url=url, to=self.telefone_destino, from_=self.telefone_origem)
        print(self.telefone_origem, self.telefone_destino)



#twilio_service = TwilioService()
#twilio_service.realiza_chamada("essa eh mensagem do botao")