# pypayments

**pypayments** é uma biblioteca idealizada para facilitar a utilização dos principais meios de pagamentos online em Python 3, neste primeiro momento apenas o **Ebanx** está disponível, mas vamos adicionar novos serviços **em breve**.

## Versão do Python

Python >= 3.5

## Dependências

*`Biblioteca requests` <br/>
pip install requests

## Para instalar

**pip install pypayments**

## Para fazer o upgrade

**pip install pypayments --upgrade**

## Chamando a biblioteca

**`from pypayments import *`**

## Passando os parâmetro de conexão

* `payment = Config(key=key,mode=mode,gateway=gateway)` - Recebe valor da chave(key) e o modo sandobox(mode=1), se estiver em **produção**, não precisa informar o mode! O gateway por enquanto utilizamos apenas o serviço da Ebanx.

## Funções disponíveis

* `send()` - Recebe os dados para solicitar o pagamento.

* `refund()` - Recebe os dados para solicitar o reembolso de um pagamento.

* `refund_or_cancel()` - Recebe os dados para solicitar o reembolso ou um cancelamento de um pagamento.

* `cancel_refund()` - Recebe os dados para solicitar o cancelamento de um reembolso.

* `cancel()` - Recebe os dados para solicitar o cancelamento de um pagamento.

## Exemplos

* `from pypayments import *`

* `key = "xyz"`

* `payment = Config(key=key,mode=1,gateway='Ebanx')`

** Gerando um Boleto **

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
}`

Se você precisar acessar o link do boleto gerado, basta capturar: novo['payment']['boleto_url']

O resultado será: https://staging-print.ebanx.com.br/print/?hash=5d78739aa5d43d1fe5590503088bd022153b133170e8ad61

** Gerando um pagamento para cartão de crédito **

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

## Agradecimentos

* `Carlos Costa` - Mr.Web2py Brasil por todo o suporte e mentoria!
* `Grupo Web2py Brasil` - Somos poucos, porém apaixonados pelo que fazemos e um grupo acolhedor! 
