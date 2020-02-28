# -*- coding: utf-8 -*-

import requests
import json


## Only if status is Open (OP) or Pending (PE)
def cancel_payment(**kwargs):

	if kwargs.get('gateway') == 'Ebanx':
	    item = {
	        'integration_key': kwargs.get('key'),
	        'hash': kwargs.get('hash')
	    }

	    send = requests.post(kwargs.get('url')['cancel'], data=item)

	    r = send.json()

	    return r


	if kwargs.get('gateway') == 'PicPay':

		headers= {'content-type': 'application/json', 'x-picpay-token': kwargs.get('key')}

		payload = {"authorizationId" : kwargs.get('authorization_id')}

		send = requests.post('https://appws.picpay.com/ecommerce/public/payments/{}/cancellations'.format(kwargs.get('payment_code')),data=json.dumps(payload), headers=headers)

		r = send.json()

		return r