# -*- coding: utf-8 -*-

import requests
import json


def new_refund(**kwargs):

    item = {
        'integration_key': kwargs.get('key'),
        'merchant_refund_code': kwargs.get('refund_code'),
        'operation': "request",
        'amount':kwargs.get('amount'),
        'hash': kwargs.get('hash'),
        'description': kwargs.get('description')
    }

    send = requests.post(kwargs.get('url')['refund'], data=item)

    r = send.json()

    return r


def new_refund_or_cancel(**kwargs):

    item = {
        'integration_key': kwargs.get('key'),
        'merchant_refund_code': kwargs.get('refund_code'),
        'operation': "request",
        'hash': kwargs.get('hash'),
        'description': kwargs.get('description')
    }

    send = requests.post(kwargs.get('url')['refundOrCancel'], data=item)

    r = send.json()

    return r


def new_cancel_refund(**kwargs):

    item = {
        'integration_key': kwargs.get('key'),
        'merchant_refund_code': kwargs.get('refund_code'),
        'operation': "cancel"
    }

    send = requests.post(kwargs.get('url')['refund'], data=item)

    r = send.json()

    return r