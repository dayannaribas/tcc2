# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:43:53 2019

@author: d.ayanna
"""

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from decouple import config


account_sid = config('account_sid', default='', cast=str)
auth_token = config('auth_token', default='', cast=str)


def realiza_chamada(mensagem, de, para):
    client = Client(account_sid, auth_token)
    # https://www.twilio.com/labs/twimlets/echo - 
    default_url = "http://twimlets.com/echo?Twiml=%3CResponse%3E%0A%3CSay%20language%3D'pt-BR'%20voice%3D%22alice%22%3E\
    {}%3C%2FSay%3E%0A%3C%2FResponse%3E&"
    message_ = mensagem.replace(" ", "%20")
    url = default_url.format(message_)
    call = client.calls.create(url=url, to=para, from_=de)
    print(call.sid)
