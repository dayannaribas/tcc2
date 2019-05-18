# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:54:10 2019

@author: d.ayanna
"""

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from decouple import config


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = config('account_sid', default='')
auth_token = config('auth_token', default='')
service_twilio = config('service_twilio', default='')

client = Client(account_sid, auth_token)

documents = client.sync.services(service_twilio).documents.list()

for record in documents:
    print(record.data)
