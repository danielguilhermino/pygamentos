from setuptools import setup


requires = [
    'requests>=2.21.0'
]


setup(
    name='pypayments',
    packages=['pypayments'],  # this must be the same as the name above
    version='0.2.9',
    description='Unofficial library for make payments in Python',
    author='Daniel Guilhermino',
    author_email='daniel@hubtec.com.br',
    license='MIT',
    url='https://github.com/hubtec/pypayments',
    keywords=['ebanx', 'payments', 'gateway'],
    classifiers=[],
)
