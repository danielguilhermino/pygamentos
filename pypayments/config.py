# -*- coding: utf-8 -*-

from .request_payment import *
from .request_refund import *
from .cancel_payment import *

class Config:
    def __init__(self, key, mode, gateway):
        self.key = key
        self.modo = mode
        self.gateway = gateway

        self.url = {
            'direct' : 'https://api.ebanx.com.br/ws/direct',
            'capture' : 'https://api.ebanx.com.br/ws/capture',
            'cancel' : 'https://api.ebanx.com.br/ws/cancel',
            'refund': 'https://api.ebanx.com.br/ws/refund',
            'refundOrCancel' : 'https://api.ebanx.com.br/ws/refundOrCancel',
            'setCVV' : 'https://api.ebanx.com.br/ws/token/setCVV',
            'token' : 'https://api.ebanx.com.br/ws/token',
            'query' : 'https://api.ebanx.com.br/ws/query',
            'print' : 'https://api.ebanx.com.br/print'
        }

        if self.modo == 1:


            ### Sandbox
            self.url = {
                'direct' : 'https://staging.ebanx.com.br/ws/direct',
                'capture' : 'https://staging.ebanx.com.br/ws/capture',
                'cancel' : 'https://staging.ebanx.com.br/ws/cancel',
                'refund': 'https://staging.ebanx.com.br/ws/refund',
                'refundOrCancel' : 'https://staging.ebanx.com.br/ws/refundOrCancel',
                'setCVV' : 'https://staging.ebanx.com.br/ws/token/setCVV',
                'token' : 'https://staging.ebanx.com.br/ws/token',
                'query' : 'https://staging.ebanx.com.br/ws/query',
                'print' : 'https://staging.ebanx.com.br/print'
                
            }

    def send(self,**kwargs):

        new = new_payment(key=self.key,url=self.url,**kwargs)

        return new
    
    def cancel(self,**kwargs):

        new = cancel_payment(key=self.key,url=self.url,**kwargs)

        return new

    def refund(self,**kwargs):

        new = new_refund(key=self.key,url=self.url,**kwargs)

        return new

    def refund_or_cancel(self,**kwargs):

        new = new_refund_or_cancel(key=self.key,url=self.url,**kwargs)

        return new

    def new_cancel_refund(self,**kwargs):

        new = new_cancel_refund(key=self.key,url=self.url,**kwargs)

        return new