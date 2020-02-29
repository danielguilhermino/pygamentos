# pygamentos

**pygamentos** é uma biblioteca idealizada para facilitar a utilização dos principais meios de pagamentos online em Python 3, estamos com suporte para os gateways de pagamento **Ebanx** e **PicPay** no momento, mas vamos adicionar novos serviços **em breve**.

## Versão do Python

Python >= 3.5

## Dependências

*`Biblioteca requests` <br/>
pip install requests

## Para instalar

**pip install pygamentos**

## Para fazer o upgrade

**pip install pygamentos --upgrade**

## Chamando a biblioteca

**`from pygamentos import *`**

## Passando os parâmetro de conexão

* `payment = Config(key=key,mode=mode,gateway=gateway)` - Recebe valor da chave(key) e o modo sandobox(mode=1), se estiver em **produção**, não precisa informar o mode!

## Funções disponíveis

* `send()` - Recebe os dados para solicitar o pagamento.

* `refund()` - Recebe os dados para solicitar o reembolso de um pagamento.

* `refund_or_cancel()` - Recebe os dados para solicitar o reembolso ou um cancelamento de um pagamento.

* `cancel_refund()` - Recebe os dados para solicitar o cancelamento de um reembolso.

* `cancel()` - Recebe os dados para solicitar o cancelamento de um pagamento.

## Exemplos usando o gateway Ebanx

* `from pygamentos import *`

* `key = "xyz"`

* `payment = Config(key=key,mode=1,gateway='Ebanx')`

**Gerando um Boleto**

<p>
novo = payment.send(type_payment='boleto',<br />
                    name='João da Couves', <br />
                    document='886.959.180-84',<br />
                    email='jonhofcouves@gmail.com', <br />
                    address='Rua João um', <br />
                    number='900', <br />
                    phone='999998888',<br />
                    city='Rio de Janeiro',<br />
                    state='RJ',<br />
                    country='br',<br />
                    zipcode='20000-111',<br />
                    payment_code='691671504',<br />
                    currency='BRL',<br />
                    total=1200)<br />

print (novo)

</p>

O retorno será um dicionário:

* `{
  'payment': {
    'hash': '5d78739aa5d43d1fe5590503088bd022153b133170e8ad61',
    'pin': '351416861',
    'country': 'br',
    'merchant_payment_code': '69123900504',
    'order_number': None,
    'status': 'PE',
    'status_date': None,
    'open_date': '2019-09-11 04:10:02',
    'confirm_date': None,
    'transfer_date': None,
    'amount_br': '1200.00',
    'amount_ext': '1200.00',
    'amount_iof': '0.00',
    'currency_rate': '1.0000',
    'currency_ext': 'BRL',
    'due_date': '2019-09-14',
    'instalments': '1',
    'payment_type_code': 'boleto',
    'boleto_url': 'https://staging-print.ebanx.com.br/print/?hash=5d78739aa5d43d1fe5590503088bd022153b133170e8ad61',
    'boleto_barcode': '34191760070014759372714245740007880120000120000',
    'boleto_barcode_raw': '34198801200001200001760000147593721424574000',
    'pre_approved': False,
    'capture_available': None
  },
  'status': 'SUCCESS'
}`*

Se você precisar acessar o link do boleto gerado, basta capturar: novo['payment']['boleto_url']

O resultado será: https://staging-print.ebanx.com.br/print/?hash=5d78739aa5d43d1fe5590503088bd022153b133170e8ad61

**Gerando um pagamento para cartão de crédito**

<p>
novo = payment.send(type_payment='boleto',<br />
                    name='João da Couves', <br />
                    document='886.959.180-84',<br />
                    email='jonhofcouves@gmail.com', <br />
                    address='Rua João um', <br />
                    number='900', <br />
                    phone='999998888',<br />
                    city='Rio de Janeiro',<br />
                    state='RJ',<br />
                    country='br',<br />
                    zipcode='20000-111',<br />
                    payment_code='691671504',<br />
                    currency='BRL',<br />
                    total=1201.55,<br />
                    card_number="4111111111111111",<br />
                    card_name='João das Couves',<br />
                    card_due_date='12/2029',<br />
                    cvv='123')

print (novo)

</p>

O retorno será um dicionário:

* `{
  'payment': {
    'hash': '5e5865bfad7ba928f4a08dab22fd644189cf553b62e9a6e4',
    'pin': '750405144',
    'country': 'br',
    'merchant_payment_code': '691671504',
    'order_number': None,
    'status': 'CO',
    'status_date': '2020-02-28 00:58:39',
    'open_date': '2020-02-28 00:58:39',
    'confirm_date': '2020-02-28 00:58:39',
    'transfer_date': None,
    'amount_br': '1201.55',
    'amount_ext': '1201.55',
    'amount_iof': '0.00',
    'currency_rate': '1.0000',
    'currency_ext': 'BRL',
    'due_date': '2020-03-02',
    'instalments': '1',
    'payment_type_code': 'visa',
    'details': {
      'billing_descriptor': 'EBANX*YOUR NAME Company'
    },
    'transaction_status': {
      'acquirer': 'EBANX',
      'code': 'OK',
      'description': 'Accepted',
      'authcode': '42526'
    },
    'pre_approved': True,
    'capture_available': False
  },
  'status': 'SUCCESS'
},
  'status': 'SUCCESS'
}`


**Solicitando Refund parcial ou total**

`novo = payment.refund(operation='request',
						hash='5e5865bfad7ba928f4a08dab22fd644189cf553b62e9a6e4',
						amount=1000.00,# Parcial
						description='Solicitado pelo usuario',
						refund_code='691671504')`
            

O retorno será um dicionário:

`{
  'payment': {
    'hash': '5e5865bfad7ba928f4a08dab22fd644189cf553b62e9a6e4',
    'pin': '376784161',
    'country': 'br',
    'merchant_payment_code': '691671504',
    'order_number': None,
    'status': 'CO',
    'status_date': '2020-02-28 00:17:12',
    'open_date': '2020-02-28 00:17:12',
    'confirm_date': '2020-02-28 00:17:12',
    'transfer_date': None,
    'amount_br': '1000.00',
    'amount_ext': '1000.00',
    'amount_iof': '0.00',
    'currency_rate': '1.0000',
    'currency_ext': 'BRL',
    'due_date': '2020-03-02',
    'instalments': '1',
    'payment_type_code': 'visa',
    'details': {
      'billing_descriptor': 'EBANX*YOUR BRAND COMPANY'
    },
    'transaction_status': {
      'acquirer': 'EBANX',
      'code': 'OK',
      'description': 'Accepted',
      'authcode': '18742'
    },
    'pre_approved': True,
    'capture_available': False,
    'refunds': [
      {
        'id': '50000465',
        'merchant_refund_code': '691pp1504',
        'status': 'RE',
        'request_date': '2020-02-28 00:33:07',
        'pending_date': None,
        'confirm_date': None,
        'cancel_date': None,
        'amount_ext': '1000.00',
        'description': 'Solicitado pelo usuario'
      }
    ]
  },
  'refund': {
    'id': '50000465',
    'merchant_refund_code': '691pp1504',
    'status': 'RE',
    'request_date': '2020-02-28 00:33:07',
    'pending_date': None,
    'confirm_date': None,
    'cancel_date': None,
    'amount_ext': '1000.00',
    'description': 'Solicitado pelo usuario'
  },
  'operation': 'refund',
  'status': 'SUCCESS'
}`

**Solicitando Refund ou Cancelamento**

novo = payment.refund_or_cancel(operation='request',
						hash='5e585b89e151a8e9d22e3c9def1f27d359d890da3f0e5b22',
						description='Solicitado pelo usuario')

O retorno será um dicionário:

`{
  'payment': {
    'hash': '5e5858de0e09569482eb1bea94f4d44cf93f32e699118857',
    'pin': '942215124',
    'country': 'br',
    'merchant_payment_code': '69112397qw01504',
    'order_number': None,
    'status': 'CO',
    'status_date': '2020-02-28 00:03:41',
    'open_date': '2020-02-28 00:03:41',
    'confirm_date': '2020-02-28 00:03:41',
    'transfer_date': None,
    'amount_br': '1200.55',
    'amount_ext': '1200.55',
    'amount_iof': '0.00',
    'currency_rate': '1.0000',
    'currency_ext': 'BRL',
    'due_date': '2020-03-02',
    'instalments': '1',
    'payment_type_code': 'visa',
    'details': {
      'billing_descriptor': 'EBANX*YOUR BRAND COMPANY'
    },
    'transaction_status': {
      'acquirer': 'EBANX',
      'code': 'OK',
      'description': 'Accepted',
      'authcode': '83227'
    },
    'pre_approved': True,
    'capture_available': False,
    'refunds': [
      {
        'id': '50000462',
        'merchant_refund_code': None,
        'status': 'RE',
        'request_date': '2020-02-28 00:05:16',
        'pending_date': None,
        'confirm_date': None,
        'cancel_date': None,
        'amount_ext': '1200.55',
        'description': 'Solicitado pelo usuario'
      }
    ]
  },
  'refund': {
    'id': '50000462',
    'merchant_refund_code': None,
    'status': 'RE',
    'request_date': '2020-02-28 00:05:16',
    'pending_date': None,
    'confirm_date': None,
    'cancel_date': None,
    'amount_ext': '1200.55',
    'description': 'Solicitado pelo usuario'
  },
  'operation': 'refund',
  'status': 'SUCCESS'
}`

## Exemplos usando o gateway PicPay

**Gerando um pagamento**

key = "xyz"
payment = Config(key=key,gateway='PicPay')

novo = payment.send(
			firstname='João',
			lastname='da Couves',
			document='886.959.180-84',
			email='jonhofcouves@gmail.com',
			phone='999998888',
			payment_code='6341504',
			total=1201.55,
			callback='https://seuite.com.br/callback',
			return_url='https://seuite.com.br/returnurl',
			expires='2022-05-01T16:00:00-03:00'
			)


**Resposta da solicitação de pagamento**

{
  'referenceId': '6OP7804',
  'paymentUrl': 'URL',
  'qrcode': {
    'content': 'URL',
    'base64': 'data:image/png;base64,código'
  },
  'expiresAt': '2022-05-01T16:00:00-03:00'
}


**Checando o estado do pagamento**

key = "xyz"
payment = Config(key=key,gateway='PicPay')

novo = payment.info(payment_code='6OP7804')

**Resposta da solicitação sobre o estado do pagamento**

{'referenceId': '6OP7804', 'status': 'paid', 'authorizationId': código}

**Cancelando o pagamento (Refund)**

key = "xyz"
payment = Config(key=key,gateway='PicPay')

novo = payment.cancel(authorization_id=código, payment_code='6OP7804')

**Resposta Cancelamento**

{'referenceId': '6OP7804', 'cancellationId': '5e599e4613c9741f607e7afc'}

## Agradecimentos

* `Carlos Costa` - Mr.Web2py Brasil por todo o suporte e mentoria!
* `Grupo Web2py Brasil` - Somos poucos, porém apaixonados pelo que fazemos e um grupo acolhedor! 
