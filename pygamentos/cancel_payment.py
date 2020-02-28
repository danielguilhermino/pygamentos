# -*- coding: utf-8 -*-

import requests
import json


## Only if status is Open (OP) or Pending (PE)
def cancel_payment(**kwargs):


    item = {
        'integration_key': kwargs.get('key'),
        'hash': kwargs.get('hash')
    }

    send = requests.post(kwargs.get('url')['cancel'], data=item)

    r = send.json()

    return r