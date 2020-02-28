# -*- coding: utf-8 -*-

import requests
import json



def info_payment(**kwargs):

	if kwargs.get('gateway') == 'PicPay':

		headers= {'content-type': 'application/json', 'x-picpay-token': kwargs.get('key')}

		get = requests.get('https://appws.picpay.com/ecommerce/public/payments/{}/status'.format(kwargs.get('payment_code')), headers=headers)

		r = get.json()

		return r