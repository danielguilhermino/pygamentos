from setuptools import setup


requires = [
    'requests>=2.21.0'
]


setup(
    name='pygamentos',
    packages=['pygamentos'],  # this must be the same as the name above
    version='0.3.0',
    description='Unofficial library for make payments in Python',
    author='Daniel Guilhermino',
    author_email='daniel@hubtec.com.br',
    license='MIT',
    url='https://github.com/hubtec/pygamentos',
    keywords=['ebanx', 'payments', 'gateway','pagamentos','PicPay'],
    classifiers=[],
)
