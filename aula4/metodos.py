# def formar_nome(nome, sobrenome, meio=''):
#     if meio:
#         return f'{sobrenome}, {nome} {meio}'
#     return f'{sobrenome}, {nome}'
#
# print(formar_nome('Ezequiel','Bertti'))


# def soma(a, b=2, c=1, *args, **kwargs):
#     s = a + b + c
#     return s
#
# print(soma(1, 2, 3, d=1, e=1, f=12))

####
# def name(positional_only_parameters, /, positional_or_keyword_parameters,
#          *, keyword_only_parameters):
####



def endereco(rua, numero, bairro, cidade, estado):
    print(f'{rua}, {numero} - {bairro} - {cidade}/{estado}')

a = {
    'rua':    'bla',
    'numero': 123,
    'bairro': 'centro',
    'cidade': 'rio de janeiro',
    'estado': 'RJ',
}
b = ['ttt', 321, 'centro', 'sao paulo', 'sp']
c = ('ttt', 321, 'centro', 'sao paulo', 'sp')
d = 'ttt,321,centro,sao paulo,sp'.split(',')

# endereco(a['rua'], a['numero'], a['bairro'], a['cidade'], a['estado'])
# endereco(**a)
# endereco(*b)
# endereco(*c)
endereco(*d)
