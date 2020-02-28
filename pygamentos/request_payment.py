# -*- coding: utf-8 -*-

import requests
import json


def new_payment(**kwargs):

    if kwargs.get('gateway') == 'Ebanx':

        item = {
                'integration_key': kwargs.get('key'),
                'operation': "request",
                'payment': {
                    'name': kwargs.get('name'),
                    'document': kwargs.get('document'),
                    'email': kwargs.get('email'),
                    'address': kwargs.get('address'),
                    'street_number': kwargs.get('number'),
                    'phone_number': kwargs.get('phone'),
                    'city': kwargs.get('city'),
                    'state': kwargs.get('state'),
                    'country': kwargs.get('country'),
                    'zipcode': kwargs.get('zipcode'),
                    'merchant_payment_code': kwargs.get('payment_code'),
                    'currency_code': kwargs.get('currency'),
                    'amount_total': kwargs.get('total')
                }
            }

        if kwargs.get('person') == 'business':
                if kwargs.get('responsible') == None:
                    return 'Please inform the responsible'
                item['payment']['person_type'] = 'business'
                item['payment']['responsible'] = {}
                item['payment']['responsible']['name'] = kwargs.get('responsible')

        if kwargs.get('type_payment') == 'boleto':
            item['payment']['payment_type_code'] = 'boleto'
            

        ## Check if payment is creditcard!
        if kwargs.get('type_payment') == 'creditcard':
            item['payment']['customer_ip'] = kwargs.get('ip') if kwargs.get('ip') else None
            item['payment']['create_token'] = kwargs.get('create_token') if kwargs.get('create_token') else False
            if kwargs.get('token'):
                if item['payment']['create_token'] == False:
                    return 'Please set create_token = True'
                else:
                    item['payment']['token'] = kwargs.get('token')
            item['payment']['payment_type_code'] = 'creditcard'
            item['payment']['instalments'] = kwargs.get('instalments') if kwargs.get('instalments') else 1
            item['payment']['creditcard'] = {}
            item['payment']['creditcard']['card_number'] = kwargs.get('card_number')
            item['payment']['creditcard']['card_name'] = kwargs.get('card_name')
            item['payment']['creditcard']['card_due_date'] = kwargs.get('card_due_date')
            item['payment']['creditcard']['card_cvv'] = kwargs.get('cvv')



        request_body = json.dumps(item)

        send = requests.post(kwargs.get('url')['direct'], data=request_body)

        r = send.json()

        return r

    if kwargs.get('gateway') == 'PicPay':

        headers= {'content-type': 'application/json', 'x-picpay-token': kwargs.get('key')}

        payload = {
            "referenceId": kwargs.get('payment_code'),
            "callbackUrl": kwargs.get('callback'),
            "returnUrl": kwargs.get('return_url'),
            "value": kwargs.get('total'),
            "expiresAt": kwargs.get('expires'), #"2022-05-01T16:00:00-03:00",
            "buyer": {
                "firstName": kwargs.get('firstname'),
                "lastName": kwargs.get('lastname'),
                "document": kwargs.get('document'),
                "email": kwargs.get('email'),
                "phone": kwargs.get('phone')
            }
        }


        send = requests.post('https://appws.picpay.com/ecommerce/public/payments', data=json.dumps(payload), headers=headers)

        r = send.json()

        return r

