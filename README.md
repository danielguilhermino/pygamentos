# pypayments

**pypayments** é uma biblioteca idealizada para facilitar a utilização dos principais meios de pagamentos online em Python 3, neste primeiro momento apenas o **Ebanx** está disponível, mas vamos adicionar novos serviços **em breve**.

## Versão do Python

Python >= 3.5

## Para instalar

Para instalar: 

**pip install pypayments**

## Funções

Para iniciar os testes, precisamos passar a chave disponibilizada pelo serviço e informar que será utilizado **sandox** para testes.

**import pypayments as payments**

* `Conn = start(key=key,mode=mode)` - Recebe valor da chave(key) e o modo sandobox(mode=1), se estiver em **produção**, não precisa informar o mode.

* `send()` - Recebe os dados para solicitar o pagamento.

* `refund()` - Recebe os dados para solicitar o reembolso de um pagamento.

* `refund_or_cancel()` - Recebe os dados para solicitar o reembolso ou um cancelamento de um pagamento.

* `cancel_refund()` - Recebe os dados para solicitar o cancelamento de um reembolso.

* `cancel()` - Recebe os dados para solicitar o cancelamento de um cancelamento.

Logo abaixo, vamos explicar como utilizar cada função.